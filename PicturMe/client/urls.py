from django.urls import path
from . import views
urlpatterns = [
path("<int:id>/" ,views.one_client , name='all_client'),
    path('all', views.all_clients, name='all_clients' ),
]
