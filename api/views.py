import json

from flask import Blueprint, render_template

from posts import Posts

api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates_api')

POSTS_PATH = './data/posts.json'


@api_blueprint.route('/posts')
def show_all_posts():
    with open(POSTS_PATH, 'r') as file:
        data = json.load(file)
        json_file = json.dumps(data, ensure_ascii=False, indent=4)
    return render_template('all_posts_json.html', file=json_file)


@api_blueprint.route('/posts/<int:post_id>')
def show_one_post_by_id(post_id):
    post_by_id = Posts.all_posts[post_id].__dict__
    json_post_by_id = json.dumps(post_by_id, ensure_ascii=False, indent=4)
    return render_template('id_post_json.html', json_post=json_post_by_id)
