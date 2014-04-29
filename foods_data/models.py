from django.db import models
# Create your models here.
class Menu(models.Model):
	title = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.title

class Food_Item(models.Model):
	food_name = models.CharField(max_length = 200)
	#Serving_Size = models.IntegerField(default=0)
	#Calories = models.IntegerField(default=0)
	Protein = models.FloatField(default=0.0)
	Carbs = models.FloatField(default=0.0)
	Fat = models.FloatField(default=0.0)
	menus = models.ManyToManyField(Menu)
	
	def __unicode__(self):
		return self.food_name