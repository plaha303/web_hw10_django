from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .utils import get_mongo
from .models import Tag, Quote, Author
from .forms import QuoteForm, AuthorForm


def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author_detail(request, author_name):
    author = get_object_or_404(Author, fullname=author_name)
    return render(request, 'quotes/author_detail.html', context={'author': author})

@login_required
def quote(request):
    tags = Tag.objects.all()
    all_authors = Author.objects.all()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            new_quote.author = Author.objects.get(id=request.POST.get('author'))
            new_quote.save()

            return redirect(to='quotes:main')
        else:
            return render(
                request,
                'quotes/quote.html',
                {'tags': tags, 'all_authors': all_authors, 'form': form},
            )
    return render(
        request,
        'quotes/quote.html',
        {'tags': tags, 'all_authors': all_authors, 'form': QuoteForm()},
    )


@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save()
            new_author.save()
            return redirect(to='quotes:main')
        else:
            return render(
                request,
                'quotes/author.html',
                {'form': form},
            )
    return render(
        request,
        'quotes/author.html',
        {'form': AuthorForm()},
    )
