from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>', views.one_transaction, name='one_transaction'),
    path('all', views.all_transactions, name='all_transactions'),
]