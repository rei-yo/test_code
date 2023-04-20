from django.urls import path, include
from . import views

app_name = 'scraping'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('good/<int:pk>',views.good , name = 'good')
]
