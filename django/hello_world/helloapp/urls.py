from django.urls import path
from .views import helloworldview

urlpatterns = [
    path('hello/', helloworldview)
]