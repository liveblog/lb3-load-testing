import uuid
from loremipsum import get_paragraphs, get_sentences
import random


def create_items(number):
    ids = []
    items = []
    paragraphs = get_paragraphs(number)
    for i in xrange(number):
        item_id = "-%s-" % str(uuid.uuid4()).replace('-', '')
        ids.append({
            "residRef": item_id
        })
        items.append(
            {
                "resource": "items",
                "username": "editor",
                "data": {
                    "firstcreated": "2013-11-11T11:11:11+00:00",
                    "text": paragraphs[i],
                    "item_type": "text"
                },
                "id_name": item_id
            }
        )
    return ids, items


def create_blog(number_of_posts, name=None):
    blog_id = "-%s-" % str(uuid.uuid4()).replace('-', '')
    posts = []
    for i in xrange(number_of_posts):
        items_ids, items = create_items(random.randint(1, 5))
        posts += items
        posts.append(
            {
                "resource": "posts",
                "username": "editor",
                "data": {
                    "firstcreated": "2013-11-11T11:11:14+00:00",
                    "blog": blog_id,
                    "groups":
                        [{
                            "id": "root",
                            "refs": [{
                                "idRef": "main"
                            }],
                            "role": "grpRole:NEP"},
                            {
                                "id": "main",
                                "refs": items_ids,
                                "role": "grpRole:Main"
                        }]
                }
            }
        )
    blog = [
        {
            "resource": "users",
            "data": {
                "username": "editor",
                "first_name": "Victor",
                "last_name": "the Editor",
                "role": "-id Editor role-",
                "user_type": "administrator",
                "password": "editor",
                "email": "editor@other.com",
                "sign_off": "eo"
            }
        },
        {
            "resource": "blogs",
            "username": "editor",
            "data": {
                "title": name or get_sentences(1)[0],
                "versioncreated": "2014-02-03T19:34:00+0000",
                "description": "",
                "members": []
            },
            "id_name": blog_id
        }
    ]
    blog += posts
    return blog

import json
print(json.dumps(create_blog(20)))
