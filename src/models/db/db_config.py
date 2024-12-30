from flask_sqlalchemy import SQLAlchemy

from src.controller.api.backend.user_api import init_user_controller
from src.dao.user import UserDao
from src.service.user_service import UserService

db = SQLAlchemy()


def init_service_and_dao(app, db):

    user_dao = UserDao(db)
    user_service = UserService(user_dao)

    user_controller = init_user_controller(user_service)
    app.register_blueprint(user_controller)



