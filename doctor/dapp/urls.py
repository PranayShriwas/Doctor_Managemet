from django.urls import path
from dapp import views
urlpatterns = [
    # user url
    path('', views.userlogin),
    path('login_reg/', views.login_reg),
    path('usersignup/', views.usersignup),

]
