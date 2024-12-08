import logging

from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from src.models.web_result import WebResultVO
from src.models.result_code import Code
from src.service import details_service

api_bp3 = Blueprint('wx_detail_api', __name__)


@api_bp3.route('/detail/hot', methods=['GET'])
@jwt_required()
def get_hot_detail():
    if not request.is_json:
        return WebResultVO(Code.FAIL_FORMAT.value, "Request must be JSON")

    # page_index = request.args.get("page")
    # page_size = request.args.get("page_size")
    page_index = 0
    page_size = 10

    result = details_service.get_details_by_page(int(page_index), int(page_size))
    return result

@api_bp3.route('/detail/hot', methods=['GET'])
@jwt_required()
def get_sort_list():
    
