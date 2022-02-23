from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import UserTeam


# Création d'une nouvelle classe UserAdmin permettant de personnaliser
# les champs demandés lors de la création d'un nouvel utilisateur
class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    fieldsets = (
        # Ajout de team par rapport au code initial
        (None, {'fields': ('username', 'password', 'team')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
          'classes': ('wide',),
          # Nous avons ici l'affichage des champs dans l'admin
          'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'team'),
        }),
    )


admin.site.register(UserTeam, MyUserAdmin)
