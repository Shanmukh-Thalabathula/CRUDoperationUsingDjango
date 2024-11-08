from django.urls import path
from students.views import *
urlpatterns = [
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('details/<int:pk>/',details,name='details'),
    path('update/<int:pk>/',update,name='update'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('search/',search,name="search"),
]