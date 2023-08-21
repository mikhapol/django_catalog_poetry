from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

from app_users.models import User
from app_users.services import email_verification_token, send_generate_old_password, send_generate_new_password
from app_users.forms import UserRegisterForm, UserProfileForm, CustomPasswordResetForm, CustomResetConfirmForm, \
    RecoverPasswordForm


class LoginView(BaseLoginView):
    template_name = 'app_users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm

    def form_valid(self, form):
        new_user = form.save()
        new_user.is_active = False
        current_site = get_current_site(self.request)
        subject = 'Активация профиля'

        send_mail(
            subject=subject,
            message=f'Активируйте ваш профиль:'
                    f' http://{current_site.domain}/app_users/activate/'
                    f'{urlsafe_base64_encode(force_bytes(new_user.pk))}/'
                    f'{email_verification_token.make_token(new_user)}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)

    success_url = reverse_lazy('app_users:login')
    template_name = 'app_users/register.html'


class ActivateView(View):

    def get_user_from_email_verification_token(self, uid, token: str):
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                get_user_model().DoesNotExist):
            return None

        if user is not None \
                and \
                email_verification_token.check_token(user, token):
            return user
        return None

    def get(self, request, uidb64, token):
        user = self.get_user_from_email_verification_token(uidb64, token)
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('app_users:login')


class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('app_users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def recover_password_view(request):
    return render(request, 'app_users/recover_password.html')


def generate_old_password(request):
    # new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)]) # Только цифры
    new_password = User.objects.make_random_password(length=12)
    request.user.set_password(new_password)
    request.user.save()
    send_generate_old_password(request.user.email, new_password)
    return redirect(reverse('app_users:login'))


def generate_new_password(user: User):
    new_password = User.objects.make_random_password(length=12)
    user.set_password(str(new_password))
    user.save()
    send_generate_new_password(user.email, new_password)


def forget_password_view(request):
    if request.method == 'POST':
        recover_form = RecoverPasswordForm(request.POST)
        if recover_form.is_valid():
            email = recover_form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                generate_new_password(user)
                return redirect('app_users:recover_password')
            except ObjectDoesNotExist:
                form = RecoverPasswordForm()
                context = {'form': form,
                           'user_does_not_exist': recover_form.cleaned_data['email']}
                return render(request, 'app_users/random_password_form.html', context)
    else:
        form = RecoverPasswordForm()
        context = {'form': form}
        return render(request, 'app_users/random_password_form.html', context=context)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'app_users/password_reset_form.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('app_users:password_reset_done')
    email_template_name = 'app_users/password_reset_email.html'
    from_email = settings.EMAIL_HOST_USER


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomResetConfirmForm
    template_name = 'app_users/password_reset_confirm.html'
    success_url = reverse_lazy('app_users:password_reset_complete')

    def form_valid(self, form):
        # Метод, который отрабатывает при успешной валидации формы
        if form.is_valid():
            self.object = form.save()
            send_mail(
                subject='Изменения пароля.',
                message=f'Вы поменяли пароль от своего профиля {self.object.email}.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email]
            )
        return super().form_valid(form)


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'app_users/password_reset_done.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'app_users/password_reset_complete.html'
