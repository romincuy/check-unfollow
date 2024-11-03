from django.urls import path
from .views import check_unfollow

urlpatterns = [
    path('', check_unfollow, name='check_unfollow'),
]
