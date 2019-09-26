from django.urls import path, include
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
) 

urlpatterns = [
    path('', views.home),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.view_profile, name="view_profile"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('profile/edit/detailed', views.edit_detailed_profile, name="edit_profile_detailed"),
    path('change-password/', views.change_password, name="change_password"),
    path('reset-password/', PasswordResetView.as_view(), name="reset_password"),
    path('reset-password/done/', PasswordResetDoneView.as_view() , name="password_reset_done"),
    path('reset-password/confirm/<uidb64>/<token>/',
                PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]