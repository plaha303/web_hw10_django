# import os
# import django
#
# from pymongo import MongoClient
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw10_project.settings')
# django.setup()
#
# from quotes.models import Quote, Tag, Author # noqa
#
# client = MongoClient("mongodb://localhost:2700")
#
# db = client.quotes
#
# authors = db.authors.find()
#
# for author in authors:
#     print(author)

import os

import django
from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw10_project.settings")
django.setup()


from quotes.models import Quote, Tag, Author  # noqa


client = MongoClient("mongodb://localhost:2700")

db = client.quotes

authors = db.authors.find()

for author in authors:
    print(author)
    