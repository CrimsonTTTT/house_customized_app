import os
import logging
from datetime import timedelta
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_jwt_extended import JWTManager

from src.controller.api.api import api_bp
from src.controller.api.house_detail_api import api_bp2
from src.models.db.db_config import db

app = Flask(__name__)
app.register_blueprint(api_bp)
app.register_blueprint(api_bp2)

# 配置 MySQL 数据库 --------------------------------------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@20.4.2.137:3306/house_customized'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)    # 初始化数据库

with app.app_context():
    db.create_all()  # 创建数据库表

# -------------------------------------------------------------------------------------------------

# JWT配置，访问受保护的接口时需要再头部增加 Authorization：Bearer + 《jwt_token》
app.config['JWT_SECRET_KEY'] = 'Gray-cat_secret_key'  # 设置jwt秘钥
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=60)  # 设置令牌过期时间为60分钟
jwt = JWTManager(app)

# 日志设置
if not app.debug:  # 仅在非调试模式下记录日志
    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler('logs/flask_app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)       # 日志级别
    app.logger.info('Flask App Startup')


@app.route('/')
def hello_world():  # put application's code here
    app.logger.info("test info msg.")
    return 'Hello World!'


if __name__ == '__main__':
    app.run()