from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User, Group

# from apps.usuarios.models import User


#-- Registrar Usuario ------------------------------------------------------------------------------------------------
class RegistroUsuarioForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'password1',
            'password2'
        ]

    #-- Al crear un nuevo usuario este queda activo por defecto.
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = True
        if commit:
            user.save()
        return user


class EditarUsuarioForm(UserChangeForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
        ]


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name"]
