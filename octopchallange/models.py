from django.db import models

class Reading(models.Model):
	mpan = models.IntegerField()
	meter_id = models.CharField(max_length=10)
	meter_register = models.CharField(max_length=2)
	reading_date_time = models.DateTimeField()
	register_reading = models.DecimalField(max_digits=10, decimal_places=1)