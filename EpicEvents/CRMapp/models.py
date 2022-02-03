from django.db import models
from authentication.models import UserTeam

class EventStatus(models.Model):
	status = models.CharField(max_length=25)


class Client(models.Model):
	STATUS_CHOICES = [('Potentiel', 'Potentiel'),
					  ('Existant', 'Existant')]
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=20)
	mobile = models.CharField(max_length=20)
	company_name = models.CharField(max_length=250)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField()
	sales_contact = models.ForeignKey(UserTeam, on_delete=models.CASCADE)
	client_status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Contract(models.Model):
	sales_contact = models.ForeignKey(UserTeam, on_delete=models.CASCADE)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField()
	status = models.BooleanField()
	amount = models.FloatField()
	payment_due = models.DateTimeField()


class Event(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField()
	# Attention pas de on delete cascade enfin je pense
	support_contact = models.ForeignKey(UserTeam, on_delete=models.CASCADE)
	event_status = models.ForeignKey(EventStatus, on_delete=models.CASCADE)
	attendees = models.IntegerField()
	event_date = models.DateTimeField()
	notes = models.CharField(max_length=100)


