from django.urls import path
from . import views
from django.contrib import admin

app_name    = "visualization"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
]