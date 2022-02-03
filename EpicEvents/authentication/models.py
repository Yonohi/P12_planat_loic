from django.contrib.auth.models import AbstractBaseUser, AbstractUser, User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


# Mettre proxy a True permet de créer des modèles mandataire de la classe mère

class UserTeam(AbstractUser):
	TEAM_ROLE = [('Management', 'Gestion'),
				 ('Support', 'Support'),
				 ('Sale', 'Vente')]
	team = models.CharField(max_length=40, choices=TEAM_ROLE)
	class Meta:
		verbose_name = "Utilisateur team"