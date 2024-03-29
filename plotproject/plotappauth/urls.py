from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('changepassword/', views.ChangePasswordView.as_view(), name="changepassword"),

]
