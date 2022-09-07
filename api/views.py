import json
import logging

from flask import Blueprint, jsonify
from classes import Posts
from utils import get_all_posts
from config import *

api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates_api')


api_logger = logging.getLogger('api_logger')
api_logger.setLevel(logging.INFO)

api_handler = logging.FileHandler('logs/api.log')

api_handler.setLevel(logging.INFO)

strfmt = '[%(asctime)s] [%(levelname)s] > %(message)s'

datefmt = '%Y-%m-%d %H:%M:%S'

api_formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)

api_handler.setFormatter(api_formatter)

api_logger.addHandler(api_handler)


@api_blueprint.route('/posts')
def show_all_posts():
    api_logger.info('Запрос /api/posts')
    data = get_all_posts(POSTS_PATH)
    return jsonify(data)


@api_blueprint.route('/posts/<int:post_id>')
def show_one_post_by_id(post_id):
    api_logger.info(f'Запрос /api/posts/{post_id}')
    post_by_id = Posts.all_posts[post_id].__dict__
    return jsonify(post_by_id)
