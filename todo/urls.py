from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('add1', views.addTodo1, name='add1'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deletecomplete1', views.deleteCompleted1, name='deletecomplete1'),
    path('deleteall1', views.deleteAll1, name='deleteall1'),
    path('deleteall', views.deleteAll, name='deleteall')
]
