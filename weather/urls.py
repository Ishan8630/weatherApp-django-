from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='base'),
    path("remove_city/<name>/",views.remove_city,name = "remove_city")
]

