from flask import Blueprint, render_template, redirect, url_for, flash
from flask.views import MethodView
from models.todo import Todo
from forms.todo_forms import TodoForm
from app import db

todo_bp = Blueprint('todo', __name__)


class TodoListView(MethodView):
    def get(self):
        todos = Todo.query.all()
        return render_template('admin/todo/index.html', todos=todos)


class TodoCreateView(MethodView):
    # method 1
    def get(self):
        form = TodoForm()
        return render_template('admin/todo/create.html', form=form)

    def post(self):
        form = TodoForm()
        if form.validate_on_submit():
            item = Todo(title=form.title.data, content=form.content.data)
            db.session.add(item)
            db.session.commit()
            flash('Todo created successfully!', 'success')
            return redirect(url_for('todo.list'))
        return render_template('admin/todo/create.html', form=form)


class TodoEditView(MethodView):
    methods = ['GET', 'POST']

    def dispatch_request(self, id):
        todo = Todo.query.get(id)
        if not todo:
            flash('Todo not found', 'error')
            return redirect(url_for('todo.index'))

        form = TodoForm(obj=todo)
        if form.validate_on_submit():
            Todo.update(todo, form)
            flash('Todo updated successfully!', 'success')
            return redirect(url_for('todo.list'))

        return render_template('admin/todo/edit.html', todo=todo, form=form)


todo_bp.add_url_rule('/', view_func=TodoListView.as_view('list'))
todo_bp.add_url_rule('/create', view_func=TodoCreateView.as_view('create'))
todo_bp.add_url_rule('/edit/<int:id>', view_func=TodoEditView.as_view('edit'))
