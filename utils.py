import json

POSTS_PATH = './data/posts.json'
COMMENTS_PATH = './data/comments.json'


def get_all_posts():
    with open(POSTS_PATH, 'r') as posts:
        all_posts = json.load(posts)
        return all_posts


def get_posts_by_user(user_name):
    with open(POSTS_PATH, 'r') as file_post:
        found_posts = []
        all_posts = json.load(file_post)
        for item in all_posts:
            if item['poster_name'] == user_name:
                found_posts.append(item)
        return found_posts


def get_comments_by_post_id(post_id):
    with open(POSTS_PATH, 'r') as file_post:
        all_posts = json.load(file_post)
        for item in all_posts:
            if item['pk'] == post_id:
                post = item
    with open(COMMENTS_PATH, 'r') as file_comments:
        data = json.load(file_comments)
        comments = []
        for item in data:
            if item['pk'] == post_id:
                comments.append(item)
    return comments, post


def search_for_posts(query):
    with open(POSTS_PATH, 'r') as file_post:
        found_posts = []
        all_posts = json.load(file_post)
        for item in all_posts:
            if query in item['content']:
                found_posts.append(item)
        return found_posts


def get_post_by_pk(pk):
    '''– возвращает один пост по его идентификатору.'''
    pass
