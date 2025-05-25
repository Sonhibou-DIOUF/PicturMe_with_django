from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>', views.one_picture , name='one_picture' ),
    path('all/',views.all_picture , name='all_picture' ),

]