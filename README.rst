Getting Started
===============

1. Create VirtualEnv

   mkproject meal-planner::

2. Clone the repo

3. Start virtual env
   
   workon Meal-Plan [tab complete]::

4. install the reqs.

   sudo pip -r install base.txt


Populating the database for Dev
===============================

1. Run the django shell then run populate.py

   python manage.py shell::
   execfile('populate.py')::
