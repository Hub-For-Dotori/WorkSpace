from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index), # ''로 들어오면 views의 index로 접근
    path('create/', views.create),
    path('read/<id>/', views.read), #<'이름'>으로 가변 값 지정 가능
    path('update/<id>/', views.update),
    path('delete/', views.delete), 
]
