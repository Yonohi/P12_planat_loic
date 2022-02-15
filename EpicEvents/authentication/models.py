from django.contrib.auth.models import AbstractUser
from django.db import models


class UserTeam(AbstractUser):
	TEAM_ROLE = [('Management', 'Gestion'),
				 ('Support', 'Support'),
				 ('Sale', 'Vente')]
	team = models.CharField(max_length=40, choices=TEAM_ROLE, blank=True)
	class Meta:
		verbose_name = "Utilisateur team"
		default_permissions = ()

	def __str__(self):
		return self.username