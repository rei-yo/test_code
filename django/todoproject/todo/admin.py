from django.contrib import admin
from .models import TodoModel, Category

admin.site.register(Category)
admin.site.register(TodoModel)

# Register your models here.
