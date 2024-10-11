from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from src.models.db.user import User, db
from src.models.web_result import WebResultVO
from src.models.result_code import Code
from src.service import login_service

api_bp = Blueprint('api', __name__)


@api_bp.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return WebResultVO(Code.FAIL_FORMAT, "Request must be JSON")

    request_data = request.get_json()
    username = request_data.get('username')
    password = request_data.get('password')
    result = login_service.login(username, password)
    return result


@api_bp.route('/user', methods=['POST'])
def create_user():
    if not request.is_json:
        return WebResultVO(Code.FAIL_FORMAT, "Request must be JSON")

    new_user = User(username="user1", password="password1")
    db.session.add(new_user)
    db.session.commit()
    return "success"


@api_bp.route('/slideImg', methods=['GET'])
def get_index_slide_images():
    result_images = [
        "http://xxx.com/img1",
        "http://xxx.com/img2",
        "https://xxx.com/img3"
    ]
    return WebResultVO(Code.SUCCESS.value, result_images).to_dict()


# =====================以下为测试用===========================================================

@api_bp.route('/protect', methods=['GET'])
@jwt_required()
def test_jwt():
    # 获取当前用户身份
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# 可以实现基于角色的访问控制，使用@jwt_required()并检查用户的角色。
@api_bp.route('/admin', methods=['GET'])
@jwt_required()
def test_admin_route():
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({"msg": "Admins only!"}), 403
    return jsonify(msg="Welcome, Admin!"), 200
