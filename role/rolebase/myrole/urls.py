from django.urls import path
from . import views

urlpatterns = [
    path('hod/signup/', views.hod_signup, name='hod_signup'),
    path('principal/signup/', views.principal_signup, name='principal_signup'),
    path('student/signup/', views.student_signup, name='student_signup'),
    path('staff/signup/', views.staff_signup, name='staff_signup'),
    path('login/', views.user_login, name='login'),
    path('hod/dashboard/', views.hod_dashboard, name='hod_dashboard'),
    path('principal/dashboard/', views.principal_dashboard, name='principal_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('',views.home,name='Home_Pge'),
    path('auth',views.auth, name ="auths")
]
