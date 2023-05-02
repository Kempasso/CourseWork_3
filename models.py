from app import db

class Posts(db.Model):
    id = db.Integer()
    poster_name = db.String
    poster_avatar = db.String
    pic = db.String
    content = db.String
    views_count = db.Integer
    likes_count = db.Integer
    pk =
