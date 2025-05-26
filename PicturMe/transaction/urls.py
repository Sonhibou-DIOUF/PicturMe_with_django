from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_transaction, name='add_transaction'),
    path('<int:id>', views.one_transaction, name='one_transaction'),
    path('all', views.all_transactions, name='all_transactions'),
]