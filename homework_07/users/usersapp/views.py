import datetime

from django.shortcuts import render

from usersapp.models import User


def main_page(request):
    users = User.objects.all()
    context = {
        'now': datetime.datetime.now(),
        'users': users,
    }
    return render(request, 'usersapp/index.html', context=context)
