# Energy Modeling Web Application

This is a simple web application built for the VEIC Energy Modeling Software Engineer interview exercise. It provides a user-friendly interface for interacting with an existing SQLite database containing energy efficiency projects and associated measures.

## Features

- View all projects and measures in the database
- Add new projects and measures through intuitive forms
- Delete existing projects (along with associated measures)
- Built with Flask, SQLAlchemy, and SQLite

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/veic-energy-app.git
cd veic-energy-app
```

2. **Create and activate a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages:**

```bash
pip install flask sqlalchemy
```

4. **Run the application:**

```bash
python app.py
```

Then open your browser and go to [http://localhost:5000](http://localhost:5000)

## Project Structure

```
├── app.py                     # Main Flask app
├── db/
│   └── application_example.db # Provided SQLite database
├── src/
│   └── app/
│       └── models.py          # SQLAlchemy models
├── templates/                 # HTML templates
├── static/
│   └── style.css              # Optional CSS styling
├── environment.yml            # (Optional) Conda environment file
└── README.md
```

## Notes

- All database interaction is handled using SQLAlchemy ORM.
- Project and Measure data are tied together via a foreign key relationship.
- This app is intended as a simple demonstration and does not include authentication, validation beyond required fields, or deployment configurations.