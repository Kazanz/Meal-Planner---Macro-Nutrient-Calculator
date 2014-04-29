from django.contrib import admin
from foods_data.models import Food_Item, Menu

class inlined(admin.TabularInline):
	model = Food_Item
	Extra = 1

class Food_Item_display(admin.ModelAdmin):
	fieldsets = [
		('Info',	{'fields':['food_name','Protein','Carbs','Fat']}),
	] 
	search_fields = ['food_name']

# Register your models here.
admin.site.register(Food_Item, Food_Item_display)
admin.site.register(Menu)