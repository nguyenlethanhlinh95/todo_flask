from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import secrets

# connect mysql
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/flask'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = secrets.token_hex(16)

# views blueprint
from views.todo import todo_bp
app.register_blueprint(todo_bp,  url_prefix='/todo')


# migration
migrate = Migrate(app, db)
migrate.init_app(app, db)


@app.route('/')
def hello():
    return '<h1>Hello, World1234!</h1>'


if __name__ == '__main__':
    app.run(debug=True)