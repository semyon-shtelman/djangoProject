from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.core.mail import send_mail

from .forms import CustomCreationForm, CustomAuthenticationForm, CustomChangeForm
from .models import User


class CustomLoginView(LoginView):
    """Представление для входа пользователя"""
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:product_list')


class CustomLogoutView(LogoutView):
    """Представление для выхода пользователя"""
    next_page = reverse_lazy('catalog:product_list')

class CustomRegisterView(FormView):
    """Представление для регистрации пользователя"""
    form_class = CustomCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        """Валидирет форму перед отправкой письма"""
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        """Метод отправки письма пользователю после регистрации"""
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = ''
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class ProfileUpdateView(UpdateView):
    model = User
    form_class = CustomChangeForm
    template_name = 'users/profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.object.pk})

class ProfileDetailView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'