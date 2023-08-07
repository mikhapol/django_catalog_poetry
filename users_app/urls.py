from django.urls import path

from users_app.apps import UsersAppConfig
from users_app.views import LoginView, LogoutView, RegisterView, ProfileUpdateView, generate_new_password

app_name = UsersAppConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
]

