from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from foods_data.models import Food_Item, Menu
from django.core.urlresolvers import reverse
from users.models import Plan_User
from django.db.models import Max

#Make your views here

def list(request):
	"""Gets the menues to display in the list.html template. """
	context = RequestContext(request)
	
	#Gets Menus
	main = Menu.objects.get(pk=1) #pk 1 is the Main Menu made in getList.py
	main_menu = main.food_item_set.all()
	
	mine = Menu.objects.get(pk=2) #pk 2 is the My Menu made in getList.py
	my_menu = mine.food_item_set.all()
	
	#Calculates My Menu totals
	pro_tot = 0
	carb_tot = 0
	fat_tot = 0
	for entry in my_menu:
		pro_tot += entry.Protein
		carb_tot += entry.Carbs
		fat_tot += entry.Fat
		
	#Gets User Macro Nutrient needed based on totals
	maxid = Plan_User.objects.aggregate(Max('id'))
	p = Plan_User.objects.get(pk = maxid['id__max'])
	cal = p.calories_needed
	fat = p.fats_needed - fat_tot
	carb = p.carbs_needed - carb_tot
	pro = p.protein_needed - pro_tot
	user = p.name + ' ' + p.name_last
	
	return render_to_response('foods_data/list.html', 
							  {'main_menu':main_menu, 'my_menu':my_menu, 'user':user, 
							   'cal':cal, 'fat':fat, 'carb':carb, 'pro':pro},
							  context
							  )
	
def add(request):
	"""Adds the selected item to My Menu."""
	if request.method == "POST":
		mine = Menu.objects.get(pk=2) #pk 2 is the My Menu made in getList.py
		f_name = request.POST.get("choice")
		food_entry = Food_Item.objects.get(food_name=f_name)
		food_entry.menus.add(mine)
			
	return HttpResponseRedirect(reverse("list:list"))
	

def remove(request):
	"""Removes the selected item from My Menu"""
	if request.method == "POST":
		mine = Menu.objects.get(pk=2) #pk 2 is the My Menu made in getList.py
		f_name = request.POST.get("choice")
		food_entry = Food_Item.objects.get(food_name=f_name)
		food_entry.menus.remove(mine)
			
	return HttpResponseRedirect(reverse("list:list"))	
	
