from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Hod, Principal, Student, Staff

class HodSignupForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    department = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'hod'
        if commit:
            user.save()
            Hod.objects.create(user=user, name=self.cleaned_data['name'], department=self.cleaned_data['department'])
        return user


class PrincipalSignupForm(UserCreationForm):
    name = forms.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'principal'
        if commit:
            user.save()
            Principal.objects.create(user=user, name=self.cleaned_data['name'])
        return user


class StudentSignupForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    year = forms.IntegerField()
    department = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'student'
        if commit:
            user.save()
            Student.objects.create(user=user, name=self.cleaned_data['name'], year=self.cleaned_data['year'], department=self.cleaned_data['department'])
        return user


class StaffSignupForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    department = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'staff'
        if commit:
            user.save()
            Staff.objects.create(user=user, name=self.cleaned_data['name'], department=self.cleaned_data['department'])
        return user
