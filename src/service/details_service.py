from src.models.db.detail import Detail, db
from src.models.result_code import Code
from src.models.web_result import WebResultVO


def create_detail(title, description, cover_img, *imgs):
    new_detail = Detail(title=title, description=description, cover_img=cover_img, imgs=imgs)
    db.session.add(new_detail)
    db.session.commit()
    return WebResultVO("done", 200).to_dict()


# 存在问题，小数据量问题不大， 大数据时此接口容易引发问题！！！！！！！！！
def get_all_details():
    db_details = Detail.query.all()
    # 将每个对象转换为字典
    detail_list = [detail.to_dict() for detail in db_details]
    return detail_list


def get_details_by_page(page_index, page_size):
    db_details = Detail.query.paginate(page=page_index, per_page=page_size)
    details_list = [item.to_dict() for item in db_details]
    return WebResultVO(200, details_list).to_dict()


def delete_detail_by_id(detail_id):
    db_detail = Detail.query.get(detail_id)
    if not db_detail:
        return WebResultVO(Code.FAIL_DB.value, "数据不存在").to_dict()
    db.session.delete(db_detail)
    db.session.commit()
    return WebResultVO(Code.SUCCESS.value, "Success").to_dict()


def update_detail_by_id(detail_id, title, description, cover_img, *imgs):
    db_detail = Detail.query.get(detail_id)
    if not db_detail:
        return WebResultVO(Code.FAIL_DB.value, "数据不存在").to_dict()

    # 修改用户的属性
    db_detail.title = title
    db_detail.description = description
    db_detail.cover_img = cover_img
    db_detail.imgs = imgs

    try:
        db.session.commit()
        return WebResultVO(Code.SUCCESS.value, f"Detail {detail_id} updated successfully!").to_dict()
    except Exception as e:
        db.session.rollback()  # 如果出错，回滚更改
        return WebResultVO(Code.FAIL_DB.value, f"Error updating : {e}").to_dict()

