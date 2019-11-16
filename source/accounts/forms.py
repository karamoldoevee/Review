from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput)

    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)

    email = forms.EmailField(required=True, label='Email')

    first_name = forms.CharField(max_length=200, required=False, label='Имя')

    def clean_password_confirm(self):

        password = self.cleaned_data.get("password")

        password_confirm = self.cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

        return password_confirm

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        try:
            User.objects.get(first_name=None)
            raise ValidationError('This filed cant be empty.', code='firt_name_empty_filed')
        except User.DoesNotExist:
            return first_name

    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user

    class Meta:

        model = User

        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']

class UserChangeForm(forms.ModelForm):

    avatar = forms.ImageField(label='Аватар', required=False)

    def save(self, commit=True):

        user = super().save(commit)

        self.save_profile(commit)

        return user

    def save_profile(self, commit=True):

        profile = self.instance.profile

        for field in self.Meta.profile_fields:
            setattr(profile, field, self.cleaned_data[field])

        if not profile.avatar:
            profile.avatar = None

        if commit:
            profile.save()

    def get_initial_for_field(self, field, field_name):

        if field_name in self.Meta.profile_fields:
            return getattr(self.instance.profile, field_name)

        return super().get_initial_for_field(field, field_name)

    def clean_github_profile(self):
        pass

    class Meta:

        model = User

        fields = ['first_name', 'last_name', 'email', 'avatar']

        profile_fields = ['avatar']

        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="Новый пароль", strip=False, widget=forms.PasswordInput)

    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)

    old_password = forms.CharField(label="Старый пароль", strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):

        password = self.cleaned_data.get("password")

        password_confirm = self.cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

        return password_confirm

    def clean_old_password(self):

        old_password = self.cleaned_data.get('old_password')

        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неправильный!')

        return old_password

    def save(self, commit=True):

        user = self.instance

        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user

    class Meta:

        model = User

        fields = ['password', 'password_confirm', 'old_password']