from django.db import models

# Create your models here.
class News(models.Model):
	page = models.CharField(max_length = 15)
	title = models.CharField(max_length = 100, unique = True)
	link = models.CharField(max_length = 300, unique = True)
	date = models.DateTimeField ()
	description = models.CharField(max_length = 2000)

	def __str__(self):
		return self.title

	class Meta:
		db_table = "news"