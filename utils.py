import json
from classes import *


def get_all_posts(path):
    with open(path, 'r') as posts:
        all_posts = json.load(posts)
        return all_posts


def get_posts_by_user(user_name):
    found_posts = []
    for item in Posts.all_posts.values():
        if item.poster_name == user_name:
            found_posts.append(item)
    if len(found_posts) == 0:
        return 'Такого юзера не существует'
    return found_posts


def get_comments_by_post_id(post_id, path):
    if post_id not in Posts.all_posts.keys():
        return 'Такого поста не существует'
    with open(path, 'r') as file_comments:
        data = json.load(file_comments)
        comments = []
        for item in data:
            if item['post_id'] == post_id:
                comments.append(item)
    return comments


def search_by_query(query):
    found_posts = []
    for item in Posts.all_posts.values():
        if query in item.content:
            found_posts.append(item)
    return found_posts


def save_bookmarks_json(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_to_bookmark(post_id, post_to_bookmarks, path):
    data = []
    if post_id not in list(Bookmarks.all_bookmarks.keys()):
        for item in Bookmarks.all_bookmarks.values():
            data.append(item.__dict__)
        else:
            data.append(post_to_bookmarks)
            save_bookmarks_json(path, data)
            Bookmarks(*post_to_bookmarks.values())
    else:
        del Bookmarks.all_bookmarks[post_id]
        for item in Bookmarks.all_bookmarks.values():
            data.append(item.__dict__)
        else:
            save_bookmarks_json(path, data)
