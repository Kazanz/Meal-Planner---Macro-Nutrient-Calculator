from django import forms
from users.models import Plan_User



class NewUserForm(forms.ModelForm):

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
	
	name = forms.CharField(max_length = 25, help_text="First Name:")
	name_last = forms.CharField(max_length = 25, help_text="Last Name:")
	gender = forms.CharField(max_length=7, help_text="Gender:", 
							 widget=forms.Select(choices=GENDER_CHOICES))
	age = forms.IntegerField(help_text="Age:")
	weight = forms.IntegerField(help_text="Weight (lbs):")
	height_ft = forms.IntegerField(help_text="Height(Feet):")
	height_in = forms.IntegerField(help_text="Height(Inches):")
	goal = forms.CharField(max_length=19, help_text="Goal:", 
									 widget=forms.Select(choices=GOAL_CHOICES))
	
	class Meta:
		model = Plan_User
		fields = ('name','name_last','gender','age','weight',
		          'height_ft','height_in','goal'
				 )