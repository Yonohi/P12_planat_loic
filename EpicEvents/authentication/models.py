from django.contrib.auth.models import User

# Mettre proxy a True permet de créer des modèles mandataire de la classe mère

class UserManagement(User):
	class Meta:
		verbose_name = 'Utilisateur Gestion'
		verbose_name_plural = 'Utilisateurs Gestion'

class UserSale(User):
	class Meta:
		verbose_name = 'Utilisateur Vente'
		verbose_name_plural = 'Utilisateurs Vente'


class UserSupport(User):
	class Meta:
		verbose_name = 'Utilisateur Support'
		verbose_name_plural = 'Utililsateurs Support'