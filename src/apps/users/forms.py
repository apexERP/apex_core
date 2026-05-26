from django import forms

from .models import Users


class EmailResetForm(forms.Form):
    email = forms.EmailField()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email']


class PasswordChangeForm(forms.Form):
    
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        
        self.user = user
        super().__init__(*args, **kwargs)

    def clean(self):
        
        """
        clean_<field>() → validates one field
        clean() → validates all fields together
        """
        
        cleaned_data = super().clean()

        old_password = cleaned_data.get("old_password")
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        # 1. Check old password
        if old_password and not self.user.check_password(old_password):
            raise forms.ValidationError("Old password is incorrect")

        # 2. Check new passwords match
        if new_password and confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError("New passwords do not match")

        # 3. Prevent same password reuse
        if old_password and new_password:
            if old_password == new_password:
                raise forms.ValidationError("New password cannot be the same as old password")

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
        
        
        
        
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

