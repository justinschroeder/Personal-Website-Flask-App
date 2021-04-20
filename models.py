from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    completed = db.Column('Completed', db.DateTime)
    title = db.Column('Title', db.String())
    description = db.Column('Description', db.String())
    skills = db.Column('Skills', db.String())
    url = db.Column('GitHub Link', db.String())


    def __repr__(self):
        return f'''<Project (
        Title: {self.title} 
        Completed: {self.completed} 
        Description: {self.description} 
        Skills: {self.skills} 
        GitHub: {self.url})>'''