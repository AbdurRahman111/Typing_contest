
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_function, name='login_function'),
    path('register', views.register, name='register'),
    path('func_logout', views.func_logout, name='func_logout'),
    path('profile', views.profile, name='profile'),
    path('mycontest', views.mycontest, name='mycontest'),
    path('myearnings', views.myearnings, name='myearnings'),
    path('myresults', views.myresults, name='myresults'),

    path('email/confirmation/<str:activation_key>/', views.email_confirm, name='email_activation' ),

    # password reset
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
