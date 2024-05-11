from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Quote, Author
from .utils import get_db
from django.core.paginator import Paginator
from .forms import QuoteForm
from .utils import get_db
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from bson.objectid import ObjectId
from pymongo import DESCENDING
from datetime import datetime
from django.contrib import messages


def index(request, page=1):
    db = get_db()
    all_quotes = db.quotes.find().sort("created_at", DESCENDING)
    per_page = 10
    paginator = Paginator(list(all_quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={"quotes": quotes_on_page})


@login_required
def create(request):
    db = get_db()
    authors = list(db.authors.find())
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():

            author = db.authors.find_one(
                {"fullname": request.POST.get('author_fullname')})
            quote = {
                'quote': form.cleaned_data.get('quote'),
                'author': author['_id'],
                'created_at': datetime.now(),
                'tags': form.cleaned_data.get('tags').split(',')
            }
            db.quotes.insert_one(quote)  # Insert the quote into MongoDB
            messages.success(request, 'Quote has been added')
            return redirect(to='quotes:index')
        else:
            return render(request, 'quotes/create.html', {'form': form})
    return render(request, 'quotes/create.html', {'form': QuoteForm(), "authors": authors})


def show(request):
    return HttpResponse('show')
