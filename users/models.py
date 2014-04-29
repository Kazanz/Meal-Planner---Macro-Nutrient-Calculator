from django.db import models

# Create your models here.
GENDER_CHOICES = (
	('Male', 'Male'),
	('Female', 'Female'),
)
    
GOAL_CHOICES = (
	('Extreme Weightloss', 'Extreme Weightloss'),
	('Cutting Diet', 'Cutting Diet'),
	('Bulking Diet', 'Bulking Diet'),
	('Extreme WeightGain', 'Extreme WeightGain'),
)
    
class Plan_User(models.Model):
	name = models.CharField(max_length = 25)
	name_last = models.CharField(max_length = 25)
	gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
	age = models.IntegerField(default = 0)
	weight = models.IntegerField(default = 0)
	height_ft = models.IntegerField(default = 0)
	height_in = models.IntegerField(default=0)
	goal = models.CharField(max_length=19, choices=GOAL_CHOICES)
	
	calories_needed = models.FloatField(default=0)
	protein_needed = models.FloatField(default=0)
	fats_needed = models.FloatField(default=0)
	carbs_needed = models.FloatField(default=0)
	
	def __unicode__(self):
		return self.name + self.name_last