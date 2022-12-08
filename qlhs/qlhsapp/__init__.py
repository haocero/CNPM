from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_babelex import Babel

app = Flask(__name__)
app.secret_key = 'qiwej#%&lakgmdgm()KLKLoaskfg&&%%'


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost/qlhsdb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

admin = Admin(app=app, name='Trang quản lý', template_mode='bootstrap4')

babel = Babel(app=app)
@babel.localeselector
def get_locale():
    return 'vi'