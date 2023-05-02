from tables import BaseModel
from sqlalchemy import Integer, String, Column, Unicode


class Posts(BaseModel):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    poster_name = Column(Unicode(255))
    poster_avatar = Column(Unicode(255))
    pic = Column(Unicode(255))
    content = Column(Unicode(255))
    views_count = Column(Integer)
    likes_count = Column(Integer)
    pk = Column(Integer)
