from flask import render_template, url_for, request, redirect
from models import app, db, Project

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add-project')
def add_project():
    return render_template('projectform.html')


# @app.route('/edit-project/<id>')
# def edit_project(id):
#     project = 
#     return render_template('projectform.html', project=project)


# @app.route('/project/<id>')    
# def project_detail(id):
#     project = 
#     return render_template('detail.html', project=project)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')