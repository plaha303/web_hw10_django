from django.urls import path


from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:page>', views.main, name='root_paginate'),
    path('author/<str:author_name>', views.author_detail, name='author_detail'),
    path('quote/', views.quote, name='quote'),
    path('add-author/', views.author, name='author')
]
