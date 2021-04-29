from flask import render_template, url_for, request, redirect
from models import app, db, Project
import datetime


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


@app.route('/project/new', methods=['GET', 'POST'])
def add_project():
    projects = Project.query.all()
    if request.form:
        year, month = request.form['date'].split('-')
        date = datetime.datetime(year=int(year), month=int(month), day=1)
        new_project = Project(title=request.form['title'],
                              completed=date,
                              description=request.form['desc'],
                              skills=request.form['skills'],
                              url=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addproject.html', projects=projects)


@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    if request.form:
        project.title = request.form['title']
        project.completed = request.form['date']
        project.description = request.form['description']
        project.skills = request.form['skills-list']
        project.url = request.form['github']
        return redirect(url_for('index'))
    return render_template('editproject.html',
                           project=project,
                           projects=projects)


@app.route('/project/<id>', methods=['GET', 'POST'])    
def project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    return render_template('detail.html',
                           project=project,
                           projects=projects)


@app.route('/project/<id>/delete')
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')