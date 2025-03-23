from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base class for declarative class definitions
Base = declarative_base()

class Project(Base):
    """
    Represents an energy efficiency project.
    """
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    title = Column(String)   # Name or title of the project
    status = Column(String)  # Current status (e.g., active, completed)

    def __repr__(self):
        return f"<Project(id={self.id}, title={self.title})>"

class Measure(Base):
    """
    Represents a specific measure installed under a project.
    """
    __tablename__ = 'measure'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'))  # Link to parent project
    measure_type = Column(String)        # Description/type of the measure
    install_date = Column(Date)          # Date the measure was installed

    # Establish relationship to parent project (can access measure.project.title)
    project = relationship("Project")

    def __repr__(self):
        return f"<Measure(id={self.id}, type={self.measure_type})>"
