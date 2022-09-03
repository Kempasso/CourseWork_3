import pytest
from utils import *

from config import *


def test_get_all_posts():
    assert type(get_all_posts(POSTS_PATH)) == list

