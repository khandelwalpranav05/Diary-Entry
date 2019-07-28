from django.db import models

# Create your models here.
class Entry(models.Model):
	text = models.TextField(max_length = 250)
	date_posted = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return 'Entry Number {}'.format(self.id)

	class Meta:
		verbose_name_plural = 'entries'