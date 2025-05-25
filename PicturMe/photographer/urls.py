from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>', views.one_photographer, name='one_photographer'),
    path('all/', views.all_photographers, name='all_photographers'),

]