from src.models.db.db_config import db


class Detail(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True,)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100),  nullable=False)
    imgs = db.Column(db.String(100), nullable=False)
    cover_img = db.Column(db.String(100), nullable=False)       # 封面

    def __repr__(self):
        return f'<User {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'imgs': self.imgs,
            'cover_img': self.cover_img
        }
