import datetime

from django.shortcuts import render


def main_page(request):
    context = {
        'now': datetime.datetime.now()
    }
    return render(request, 'usersapp/index.html', context=context)
