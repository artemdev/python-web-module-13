from pymongo import DESCENDING
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm
from django.shortcuts import render, redirect
from .models import Author
from bson.objectid import ObjectId
from .utils import get_db
from datetime import datetime
from django.contrib import messages


@login_required()
def create(request):
    db = get_db()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            db.authors.insert_one(
                {'fullname': form.cleaned_data.get('fullname'),
                 'born_date': form.cleaned_data.get('born_date'),
                 'born_location': form.cleaned_data.get('born_location'),
                 'description': form.cleaned_data.get('description'),
                 'created_at': datetime.now()})

            messages.success(request, 'Author has been added')
            return redirect(to='authors:index')
        else:
            return render(request, 'authors/create.html', {'form': form})

    return render(request, 'authors/create.html', {'form': AuthorForm()})


def show(request, fullname):
    db = get_db()
    author = db.authors.find_one({"fullname": fullname})
    return render(request, 'authors/show.html', {'author': author})


def index(request):
    db = get_db()
    authors = db.authors.find().sort("created_at", DESCENDING)

    return render(request, 'authors/index.html', {"authors": authors})
