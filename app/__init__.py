from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, _

import os

app = Flask(__name__)
app.secret_key = 'super-secret-key-123'

# Настройки базы данных
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..', 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Настройки языков
app.config['BABEL_DEFAULT_LOCALE'] = 'ru'
app.config['BABEL_SUPPORTED_LOCALES'] = ['ru', 'en', 'lv']

# Инициализация Babel
babel = Babel(app)

@babel.localeselector
def get_locale():
    return session.get('lang') or request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

@app.context_processor
def inject_translations():
    return dict(_=_)

# Инициализация базы данных
db = SQLAlchemy(app)

from app import routes, models  # после создания app и db

# Login manager
from flask_login import LoginManager
from app.models import User

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Flask-Migrate
from flask_migrate import Migrate
migrate = Migrate(app, db)


from flask_babel import get_locale

# Регистрируем функцию get_locale в Jinja
app.jinja_env.globals['get_locale'] = get_locale
