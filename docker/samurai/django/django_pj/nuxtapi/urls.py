from django.urls import path
from . import views

app_name    = "nuxtapi"
urlpatterns = [
    # path('', views.index, name="index"),
    path('get_user', views.get_user_view, name='get_user'),
    # path('api/update_values/', views.update_view, name='update_val'),
]