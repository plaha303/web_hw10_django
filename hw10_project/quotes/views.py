from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .utils import get_mongo
# from .models import Author


def main(request, page=1):
    db = get_mongo()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


# def author_detail(request, author_name):
#     author = get_object_or_404(Author, fullname=author_name)
#     return render(request, 'quotes/author_detail.html', context={'author': author})