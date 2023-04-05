from app import db
from datetime import datetime


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    @classmethod
    def create(cls, todo, form):
        todo.title = form.title.data
        todo.content = form.content.data
        db.session.commit()

    @classmethod
    def update(cls, todo, form):
        todo.title = form.title.data
        todo.content = form.content.data
        db.session.commit()

    def __repr__(self):
        return f'<Todo {self.id}>'
