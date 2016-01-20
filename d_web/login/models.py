from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(object):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user_list = [
    User('vip', 'vip@dad', '123'),
    User('admin', 'admin@123', '123'),
]