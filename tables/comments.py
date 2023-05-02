from tables import BaseModel
from sqlalchemy import Integer, String, Column, Unicode


class Comments(BaseModel):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(Unicode(255))
    commenter_name = Column(Unicode(255))
    comment = Column(Unicode(255))
    pk = Column(Integer)
