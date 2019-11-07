from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.utils.translation import ugettext_lazy as _

# Create your models here.
HARDNESS_LEVEL_CHOICES = (
    ("1", "آسان"),
    ("2", "متوسط"),
    ("3", "سخت")
)


class Category(models.Model):
    name = models.CharField(max_length=200)


class Word(models.Model):
    categoris = models.ManyToManyField(Category)
    hardness_level = models.CharField(max_length=1, choices=HARDNESS_LEVEL_CHOICES)


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    first_player_name = models.CharField(max_length=50)
    second_player_name = models.CharField(max_length=50)


class Comment(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('عنوان'))
    text = models.TextField(verbose_name=_('متن'))

    class Meta:
        verbose_name = _('نظر')
        verbose_name_plural = _('نظرات')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
                               label='نام کاربری',
                               required=True,
                               disabled=False,
                               help_text='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}),
                               label='رمز عبور',
                               required=True,
                               disabled=False,
                               help_text='')

    class Meta:
        model = User
        fields = ['username', 'password']


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
                               label='نام کاربری',
                               required=True,
                               disabled=False,
                               help_text='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام'}),
                                 label='نام',
                                 required=True,
                                 disabled=False,
                                 help_text='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}),
                                label='نام خانوادگی',
                                required=True,
                                disabled=False,
                                help_text='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}),
                                label='رمز عبور',
                                required=True,
                                disabled=False,
                                help_text='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'}),
                                label='تکرار رمز عبور',
                                required=True,
                                disabled=False,
                                help_text='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
                             label='ایمیل',
                             max_length=64,
                             help_text='یک ایمیل معتبر وارد کنید')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()
    # picture = models.ImageField(upload_to='static/profile_pictures', blank=True, null=True)
    # authentication_key = models.CharField(max_length=50)
    session_key = models.CharField(null=True, blank=True, max_length=160)
    authentication_key = models.CharField(null=True, blank=True, max_length=50)


class ForgottenUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    key = models.TextField(max_length=32)


class ActivateUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    key = models.TextField(max_length=32)
