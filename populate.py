import csv
import os
import re
import collections
from foods_data.models import Food_Item, Menu

""" MAKE SURE THIS FILE AND THE fooddata.txt ARE LOCATED IN THE SAME FOLDER AS
manage.py.

Use thie script to populate database.  Run 'python manage.py shell' then run
'execfexiile('getList.py')' and watch your entries get added."""


#Defines location of txt file with data to read
#__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def getInfo():
    """returns a dicitonary whose keys are food names and who values are a list of
    nutrition data number"""
    foods = {}
    text = open(os.path.join(os.getcwd(), "fooddatashort.txt"))
    for lines in text:
        linelist = lines.split('    ')
        name = linelist[0]
        data = linelist[1:len(linelist)]
        foods[name] = data
    return foods
foodDic = getInfo()

#make menus
main_menu = Menu(title="Main Menu")
main_menu.save()
my_menu = Menu(title="My Menu")
my_menu.save()

#--- THIS IS JUST SO YOU CAN SEE WHERE IN THE LIST PROTEIN ETC ARE LOCATED IN THE TXT --#
#nutriData =foodDic.values()
#protein = nutriData[2]
#carbs = nutriData[5]
#fats = nutriData[3]

def Nutri_to_db(dictionary):
    """When run this will add all the food_items to the database."""
    for k,v in dictionary.items():
        nutri_data = v
        p = float(nutri_data[2])
        c = float(nutri_data[5])
        f = float(nutri_data[3])
        print k
        F = Food_Item(food_name=k,Protein=p,Carbs=c,Fat=f)
        F.save()
        F.menus.add(main_menu)
Nutri_to_db(foodDic)



