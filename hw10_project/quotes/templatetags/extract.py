from django import template
from bson.objectid import ObjectId
from ..utils import get_mongo

register = template.Library()


def get_author(id_):
    db = get_mongo()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    return author['fullname']


register.filter('author', get_author)
