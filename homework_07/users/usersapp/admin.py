from django.contrib import admin

from usersapp.models import User, Post

admin.site.register(User)
admin.site.register(Post)
