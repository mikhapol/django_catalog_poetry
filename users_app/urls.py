from django.urls import path

from users_app.apps import UsersAppConfig
from users_app.views import LoginView, LogoutView, RegisterView, ProfileUpdateView, generate_new_password, \
    CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, \
    CustomPasswordResetCompleteView, ActivateView, forget_password_view, recover_password_view

app_name = UsersAppConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('activate/<uidb64>/<token>', ActivateView.as_view(), name='activate'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('reset_password/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('random_password_form/', forget_password_view, name='random_password_form'),
    path('recover_password/', recover_password_view, name='recover_password'),
]
