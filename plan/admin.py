from django.contrib import admin
from .models import Todo
# Register your models here.
admin.site.register(Todo)           # admin.site에 Todo를 등록해 admin에서도 Todo를 볼수 있음.