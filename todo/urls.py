from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<str:pk>',views.delete, name='delete'),
    path('login',views.login,name = 'login'),
    path('signup', views.signup, name= 'signup'),
    path('logout', views.logout, name= 'logout'),
    path('status_task/<int:pk>/<str:status>',views.status_task, name = 'status_task')
]
