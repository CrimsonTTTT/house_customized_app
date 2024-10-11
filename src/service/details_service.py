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


def delete_detail_by_id(detail_id):
    db_detail = Detail.query.get(detail_id)
    if not db_detail:
        return WebResultVO(Code.FAIL_DB.value, "数据不存在").to_dict()
    db.session.delete(db_detail)
    db.session.commit()
    return WebResultVO(Code.SUCCESS.value, "Success").to_dict()