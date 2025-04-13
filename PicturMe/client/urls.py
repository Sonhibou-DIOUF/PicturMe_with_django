from django.urls import path
from . import views
urlpatterns = [
path('',views.hello_client , name='hello_client')
]
