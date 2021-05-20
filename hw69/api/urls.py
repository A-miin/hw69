from django.urls import path
from api.views import  add, subtract, multiply, divide,get_token_view

urlpatterns = [
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
    path('token/', get_token_view, name='token'),
]
