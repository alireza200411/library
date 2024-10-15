from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('login', views.login_user, name='login'),
    path('<int:ID>', views.display, name='display')

]
