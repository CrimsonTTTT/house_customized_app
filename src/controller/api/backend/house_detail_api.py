import logging

from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from src.models.web_result import WebResultVO
from src.models.result_code import Code
from src.service import details_service

api_bp2 = Blueprint('api_bp2', __name__)


@api_bp2.route('/detail', methods=['POST'])
@jwt_required()
def create_house_detail():
    if not request.is_json:
        return WebResultVO(Code.FAIL_FORMAT.value, "Request must be JSON")

    params = request.get_json()
    title = params.get('title')
    description = params.get('description')
    coverImg = params.get('coverImg')
    imgs = params.get('imgs')
    result = details_service.create_detail(title, description, coverImg, imgs)
    return result


@api_bp2.route('/detail', methods=['GET'])
def find_house_detail_all():
    results = details_service.get_all_details()
    return jsonify(results), 200


@api_bp2.route('/detail/page', methods=['GET'])
def find_house_detail_by_pages():
    page_index = request.args.get("page")
    page_size = request.args.get("page_size")
    result = details_service.get_details_by_page(int(page_index), int(page_size))
    return result


@api_bp2.route('/detail', methods=['DELETE'])
@jwt_required()
def delete_house_detail_by_id():
    detail_id = request.args.get('id')
    result = details_service.delete_detail_by_id(detail_id)
    current_app.logger.info(f"返回数据：{result}")
    return result


@api_bp2.route('/detail', methods=['PATCH'])
@jwt_required()
def update_detail_by_id():
    if not request.is_json:
        return WebResultVO(Code.FAIL_FORMAT.value, "Request must be JSON")

    request_data = request.get_json()
    detail_id = request_data.get('id')
    title = request_data.get('title')
    description = request_data.get('description')
    coverImg = request_data.get('coverImg')
    imgs = request_data.get('imgs')

    result = details_service.update_detail_by_id(detail_id, title, description, coverImg, imgs)
    current_app.logger.info(f"返回数据：{result}")
    return result
