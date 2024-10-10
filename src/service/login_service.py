# 登录操作，校验密码
from flask import jsonify
from flask_jwt_extended import create_access_token


def login(username, password):
    # 模拟数据库中数据
    user_db = {
        "user1": "password1",
        "user2": "password2",
    }

    # 检查用户凭据
    if username in user_db and user_db[username] == password:
        # 创建访问令牌
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401


def logout():
    pass

