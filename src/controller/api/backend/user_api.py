from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from src.models.db.user import User, db
from src.models.web_result import WebResultVO
from src.models.result_code import Code
from src.service import login_service, user_service

api_bp_user = Blueprint('api_user', __name__)


def init_user_controller(user_service):
    @api_bp_user.route('/user/register', methods=['POST'])
    @jwt_required()
    def register_user():
        if not request.is_json:
            return WebResultVO(Code.FAIL_FORMAT, "Request must be JSON")

        request_data = request.get_json()
        username = request_data.get('username')
        password = request_data.get('password')
        result = user_service.create_my_user(username, password)
        return result





