from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('single/',views.single_course,name='single'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('register/',views.signup_user,name='signup'),
    # path('recover/',views.recover,name='recover'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='app/components/recover.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='app/components/password_sent.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/components/reset_pass.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/components/reset_complete.html'),name='password_reset_complete'),

]
