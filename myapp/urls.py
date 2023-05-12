
from django.urls import path
from . import views
urlpatterns = [
    path('',views.initial),
    path('insert',views.insert,name="insert"),
    path('display',views.display,name="display"),
    path('delete_all',views.delete_all,name="delete_all"),
    path('login',views.login,name="login"),
]