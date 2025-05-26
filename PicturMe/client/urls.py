from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_client, name='add_client'),
path("<int:id>/" ,views.one_client , name='one_client'),
    path('all', views.all_clients, name='all_clients' ),
]
