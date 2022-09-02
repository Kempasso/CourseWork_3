import json


def get_all_posts(path):
    with open(path, 'r') as posts:
        all_posts = json.load(posts)
        return all_posts


def get_posts_by_user(user_name, all_posts):
    found_posts = []
    for item in all_posts.values():
        if item.poster_name == user_name:
            found_posts.append(item)
    return found_posts


def get_comments_by_post_id(post_id, path):
    with open(path, 'r') as file_comments:
        data = json.load(file_comments)
        comments = []
        for item in data:
            if item['pk'] == post_id:
                comments.append(item)
    return comments


def search_by_query(query, all_posts):
    found_posts = []
    for item in all_posts.values():
        if query in item.content:
            found_posts.append(item)
    return found_posts


def save_bookmarks_json(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_to_bookmark(post_id, post_to_bookmarks, Bookmarks, path):
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


def get_post_by_pk(pk):
    '''– возвращает один пост по его идентификатору.'''
    pass
