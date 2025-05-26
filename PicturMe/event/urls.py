from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_event, name='add_event'),
    path('<int:id>', views.one_event, name='one_event'),
    path('all/', views.all_events, name='all_events'),
]