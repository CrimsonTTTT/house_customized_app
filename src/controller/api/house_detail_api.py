from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from src.models.web_result import WebResultVO
from src.models.result_code import Code
from src.service import details_service

api_bp2 = Blueprint('house_api', __name__)


@api_bp2.route('/detail', methods=['POST'])
@jwt_required()
def create_house_detail():
    if not request.is_json:
        return WebResultVO(Code.FAIL_FORMAT, "Request must be JSON")

    params = request.get_json()
    title = params.get('title')
    description = params.get('description')
    imgs = params.get('imgs')
    result = details_service.create_detail(title, description, imgs)
    return result


@api_bp2.route('/detail', methods=['GET'])
@jwt_required()
def find_house_detail_all():
    pass


@api_bp2.route('/detail', methods=['DELETE'])
@jwt_required()
def delete_house_detail_by_id():
    pass


