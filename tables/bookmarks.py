from sqlalchemy.orm import relationship

from tables import BaseModel
from sqlalchemy import Integer, String, Column, Unicode


class Bookmarks(BaseModel):
    __tablename__ = "bookmarks"
    id = Column(Integer, primary_key=True)
    post_id = relationship("Posts", lazy="subquery")
