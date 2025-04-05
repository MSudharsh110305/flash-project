from flask import render_template, url_for, request, flash, request
from flask_login import login_required, current_user
from . import projects
from app.models  import Project
from app.extensions import db

@projects.route('/')
@login_required
def dashboard():
    projects_list = Project.query.all()
    return render_template('projects/dashboard.html', projects=projects_list)
@projects.route('/create', methods=['GET', 'POST'])
@login_required
def create_project():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        project = Project(name=name, description=description)
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully.')
        return redirect(url_for('projects.dashboard'))
    return render_template('projects/create_project.html')