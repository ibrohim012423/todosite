
from django.urls import path
from .views import create, list, asosiy, delete, korish

urlpatterns = [
    path('create/', create, name='creat'),
    path('list/', list , name='list'),
    path('', asosiy, name='asosiy'),
    path('list/delete/<int:pk>', delete.as_view(), name='udalit'),
    path('list/korish/<str:nomi>',korish, name='korish')
]
