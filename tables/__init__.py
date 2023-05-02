from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

from . import bookmarks
from . import posts
from . import comments
