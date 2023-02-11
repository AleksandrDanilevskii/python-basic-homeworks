import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from usersapp.models import User, Post


def main_page(request):
    context = {
        'now': datetime.datetime.now(),
    }
    return render(request, 'usersapp/index.html', context=context)


class UsersListView(ListView):
    model = User


class UsersDetailView(DetailView):
    model = User


class PostsListView(ListView):
    model = Post

