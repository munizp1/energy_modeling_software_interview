from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app.models import Base, Project, Measure
from datetime import datetime
import os

# Set up the path to the SQLite database
db_path = os.path.join(os.path.dirname(__file__), 'db', 'application_example.db')
engine = create_engine(f'sqlite:///{db_path}', echo=False)

# Bind the engine and set up the database session
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Initialize the Flask application
app = Flask(__name__)


# ---------- Home ----------
@app.route('/')
def index():
    # Redirect root URL to the project list
    return redirect(url_for('project_list'))


# ---------- Projects ----------
@app.route('/projects')
def project_list():
    # Retrieve and display all projects (most recent first)
    projects = session.query(Project).order_by(Project.id.desc()).all()
    return render_template('project_list.html', projects=projects)

@app.route('/projects/new', methods=['GET'])
def project_create_form():
    # Render form to create a new project
    return render_template('project_create.html')

@app.route('/projects/create', methods=['POST'])
def project_create():
    # Handle new project form submission
    title = request.form['title']
    status = request.form['status']
    new_project = Project(title=title, status=status)
    session.add(new_project)
    session.commit()
    return redirect(url_for('project_list'))

@app.route('/projects/delete/<int:project_id>', methods=['POST'])
def project_delete(project_id):
    # Delete a project and its associated measures
    project = session.query(Project).get(project_id)
    if project:
        session.query(Measure).filter_by(project_id=project.id).delete()
        session.delete(project)
        session.commit()
    return redirect(url_for('project_list'))


# ---------- Measures ----------
@app.route('/measures')
def measure_list():
    # Display all measures (most recent first)
    measures = session.query(Measure).order_by(Measure.id.desc()).all()
    return render_template('measure_list.html', measures=measures)

@app.route('/measures/new', methods=['GET'])
def measure_create_form():
    # Render form to create a new measure
    projects = session.query(Project).all()
    return render_template('measure_create.html', projects=projects)

@app.route('/measures/create', methods=['POST'])
def measure_create():
    # Handle new measure form submission
    project_id = request.form['project_id']
    measure_type = request.form['measure_type']
    install_date = datetime.strptime(request.form['install_date'], '%Y-%m-%d').date()

    new_measure = Measure(
        project_id=project_id,
        measure_type=measure_type,
        install_date=install_date
    )
    session.add(new_measure)
    session.commit()
    return redirect(url_for('measure_list'))

@app.route('/measures/delete/<int:measure_id>', methods=['POST'])
def measure_delete(measure_id):
    # Delete a single measure
    measure = session.query(Measure).get(measure_id)
    if measure:
        session.delete(measure)
        session.commit()
    return redirect(url_for('measure_list'))


if __name__ == '__main__':
    app.run(debug=True)
