from django.db import models
from authentication.models import UserTeam
from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Please enter a phone number.")

class EventStatus(models.Model):
	status = models.CharField(max_length=25,unique=True)
	class Meta():
		verbose_name = "Event Status"
		verbose_name_plural = "Event Status"

	def __str__(self):
		return f"{self.status}"

class Client(models.Model):
	STATUS_CHOICES = [('Potentiel', 'Potentiel'),
					  ('Existant', 'Existant')]
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=15, validators=[phone_regex])
	mobile = models.CharField(max_length=15, validators=[phone_regex])
	company_name = models.CharField(max_length=250)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	# limit_choices_to nous permet ici de limiter les possibilités à l'équipe
	# de Vente
	sales_contact = models.ForeignKey(UserTeam, limit_choices_to={'team': 'Sale'},on_delete=models.CASCADE)
	client_status = models.CharField(max_length=20, choices=STATUS_CHOICES)

	def __str__(self):
		return f"id:{self.id} {self.first_name} {self.last_name}"


class Contract(models.Model):
	sales_contact = models.ForeignKey(UserTeam, limit_choices_to={'team': 'Sale'}, on_delete=models.CASCADE)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	status = models.BooleanField()
	amount = models.FloatField()
	payment_due = models.DateTimeField()

	def __str__(self):
		return f"Contract {self.id} ({str(self.client)})"


class Event(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	# Attention pas de on delete cascade enfin je pense
	support_contact = models.ForeignKey(UserTeam, limit_choices_to={'team': 'Support'}, on_delete=models.CASCADE)
	event_status = models.ForeignKey(EventStatus, on_delete=models.CASCADE)
	attendees = models.IntegerField()
	event_date = models.DateTimeField()
	notes = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return f"Event {self.id} ({str(self.client)})"



