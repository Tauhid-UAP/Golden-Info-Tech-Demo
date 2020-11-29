from django.urls import path
from . import views

# app_name='features'

urlpatterns = [

    path('member_list/', views.member_list, name='member_list'),
    path('member_transactions/<int:id>', views.member_transactions, name='member_transactions'),

]