from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import *
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register([Talaba,Muallif,Kutubxonachi,Kitob,Record])
