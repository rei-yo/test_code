from django.urls import path
from . import views

app_name    = "bbs"
urlpatterns = [
    path('', views.index, name="index"),
    path("single/<int:pk>/", views.single, name="single"),
    path('album/', views.album, name="album"),
    path('document/', views.document, name="document"),
]