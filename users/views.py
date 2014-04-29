from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from users.models import Plan_User
from users.forms import NewUserForm
from django.core.urlresolvers import reverse
from users.MacroCalc import calcXLoss, calcCutting, calcBulking, calcXGain
from django.db.models import Max

# Create your views here.
def add_new_user(request):
	context = RequestContext(request)  #Look up what this does
	form = NewUserForm()
	return render_to_response('users/add_new_user.html',
							 {'form': form}, context)
	
#Adds the user to the database then redirects to the thank you page
def adding(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			values = {}
			
			#These if statements do the Macro Calculations based on goal input
			if form.cleaned_data['goal'] == 'Extreme Weightloss':
				values = calcXLoss(form.cleaned_data['weight'])
			elif form.cleaned_data['goal'] == 'Cutting Diet':
				values = calcCutting(form.cleaned_data['weight'])
			elif form.cleaned_data['goal'] == 'Bulking Diet':
				values = calcBulking(form.cleaned_data['weight'])
			else:
				values = calcXGain(form.cleaned_data['weight'])
			
			#this code saves the new user to the database
			new_user = Plan_User(name=form.cleaned_data['name'],
								 name_last=form.cleaned_data['name_last'],
								 gender=form.cleaned_data['gender'],
								 age=form.cleaned_data['age'],
								 weight=form.cleaned_data['weight'],
								 height_ft=form.cleaned_data['height_ft'],
								 height_in=form.cleaned_data['height_in'],
								 goal=form.cleaned_data['goal'],
								 calories_needed=values['cal'],
								 protein_needed=values['pro'],
								 fats_needed=values['fat'],
								 carbs_needed=values['carb'],
								 )
			new_user.save()

		else:
			return HttpResponse("Something went wrong.  Please go back and try again")
	else:
			return HttpResponse("Something went wrong.  Please go back and try again")
							
	return HttpResponseRedirect(reverse('list:list'))
	
	
	
	