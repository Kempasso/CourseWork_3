from flask import Flask, render_template, request

from Posts import Posts
from utils import *

app = Flask(__name__)

all_posts = get_all_posts()
for i in all_posts:
    Posts(*i.values())


@app.route('/', methods=['GET'])  # Index HTML / Список всех имеющихся постов
def main_page():
    all_posts = get_all_posts()
    return render_template('index.html', all_posts=all_posts)


@app.route('/posts/<int:post_id>', methods=['GET'])
def search_by_id(post_id):
    comments, post = get_comments_by_post_id(post_id)
    return render_template('post.html', comments=comments, post=post, count_comments=len(comments))


@app.route('/search', methods=['GET'])
def search_by_query():
    query = request.args.get('query')
    found_posts = search_for_posts(query)
    return render_template('search.html', found_posts=found_posts)


@app.route('/users/<user_name>', methods=['GET'])
def get_user_posts(user_name):
    found_posts = get_posts_by_user(user_name)
    return render_template('user-feed.html', found_posts=found_posts)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


app.run()
