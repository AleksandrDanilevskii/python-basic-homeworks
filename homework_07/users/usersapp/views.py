import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from usersapp.models import User


def main_page(request):
    users = User.objects.all()
    context = {
        'now': datetime.datetime.now(),
        'users': users,
    }
    return render(request, 'usersapp/index.html', context=context)


class UsersListView(ListView):
    model = User


class UsersDetailView(DetailView):
    model = User
