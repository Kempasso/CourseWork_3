from flask import request, redirect, Flask, render_template

from api.views import *
from config import *
from utils import *

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/api')
app.config['JSON_AS_ASCII'] = False

all_posts = get_all_posts(POSTS_PATH)
for i in all_posts:
    Posts(*i.values())
all_bookmarks = get_all_posts(BOOKMARKS_PATH)
for x in all_bookmarks:
    Bookmarks(*x.values())


@app.route('/', methods=['GET'])  # Index HTML / Список всех имеющихся постов
def main_page():
    return render_template('index.html', all_posts=Posts.all_posts, count=len(Bookmarks.all_bookmarks))


@app.route('/', methods=['POST'])
def add_delete_bookmarks():
    post_id = int(request.form.get('book'))
    post_to_bookmarks = Posts.all_posts.get(post_id).__dict__
    add_to_bookmark(post_id, post_to_bookmarks, BOOKMARKS_PATH)
    return redirect("/", code=302)


@app.route('/posts/<int:post_id>', methods=['GET'])
def search_by_id(post_id):
    comments = get_comments_by_post_id(post_id, COMMENTS_PATH, )
    if type(comments) == str:
        return comments
    post = Posts.all_posts[post_id]
    post.views_count += 1
    return render_template('post.html', comments=comments, post=post, count_comments=len(comments))


@app.route('/search', methods=['GET'])
def get_found_post():
    query = request.args.get('query')
    found_posts = search_by_query(query)
    return render_template('search.html', found_posts=found_posts)


@app.route('/users/<user_name>', methods=['GET'])
def get_user_posts(user_name):
    found_posts = get_posts_by_user(user_name)
    if type(found_posts) == str:
        return f'{found_posts}'
    return render_template('user-feed.html', found_posts=found_posts)


@app.route('/bookmarks', methods=['GET'])
def show_bookmarks():
    return render_template('bookmarks.html', bookmarks=Bookmarks.all_bookmarks)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run()
