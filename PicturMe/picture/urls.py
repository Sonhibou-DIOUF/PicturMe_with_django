from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_picture, name='add_picture'),
    path('<int:id>', views.one_picture , name='one_picture' ),
    path('all/',views.all_pictures , name='all_pictures' ),

]