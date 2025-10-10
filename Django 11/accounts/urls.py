from django.urls import path
from .views import auth_view

app_name = 'accounts'

urlpatterns = [
    path('', auth_view, name='auth'),
]
