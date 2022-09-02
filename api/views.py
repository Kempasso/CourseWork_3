import json

from flask import Blueprint, render_template, Flask
import logging
from classes import Posts

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

POSTS_PATH = './data/posts.json'


@api_blueprint.route('/posts')
def show_all_posts():
    api_logger.info('Запрос /api/posts')
    with open(POSTS_PATH, 'r') as file:
        data = json.load(file)
        json_file = json.dumps(data, ensure_ascii=False, indent=4)
    return render_template('all_posts_json.html', file=json_file)


@api_blueprint.route('/posts/<int:post_id>')
def show_one_post_by_id(post_id):
    api_logger.info(f'Запрос /api/posts/{post_id}')
    post_by_id = Posts.all_posts[post_id].__dict__
    json_post_by_id = json.dumps(post_by_id, ensure_ascii=False, indent=4)
    return render_template('id_post_json.html', json_post=json_post_by_id)
