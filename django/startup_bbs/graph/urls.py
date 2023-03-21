from django.urls import path
from . import views

app_name    = "graph"
urlpatterns = [
    path('', views.index, name="index"),
    path('api/get_values/', views.get_values, name='get_val'),
    path('api/update_values/', views.update_view, name='update_val'),
]