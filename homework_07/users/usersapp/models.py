from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name='name', max_length=64)
    username = models.CharField(verbose_name='username', max_length=32, unique=True)
    email = models.CharField(verbose_name='email', max_length=64, unique=True)
    address = models.TextField(verbose_name='address', blank=True)
    phone = models.CharField(verbose_name='phone', max_length=20, blank=True)
    website = models.CharField(verbose_name='website', max_length=64, blank=True)
    company = models.CharField(verbose_name='company', max_length=64, blank=True)

    def __str__(self):
        return f'{self.name} ({self.username})'
