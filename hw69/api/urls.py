from django.urls import path
from api.views import json_echo_view, add, subtract, multiply, divide,get_token_view

urlpatterns = [
    path('date/', json_echo_view , name='date'),
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
    path('token/', get_token_view, name='token'),
]
