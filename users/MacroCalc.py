
def calcCutting(weight):
	calories_needed = weight * 16 - 500
	protein_needed = round(weight * 1.5,2)
	protein_cals = protein_needed * 4
	fats_cals = calories_needed * .25
	fats_needed = round(fats_cals / 9,2)
	carbs_cals = calories_needed - protein_cals - fats_cals
	carbs_needed = round(carbs_cals / 4,2)
	calories_rounded = round(calories_needed,2)
	
	values = {'cal': calories_rounded, 'pro': protein_needed, 'fat': fats_needed,
			  'carb': carbs_needed}

	return values
	
def calcBulking(weight):
	calories_needed = weight * 16
	protein_needed = round(weight * 1.5,2)
	protein_cals = protein_needed * 4
	fats_cals = calories_needed * .25
	fats_needed = round(fats_cals / 9,2)
	carbs_cals = calories_needed - protein_cals - fats_cals
	carbs_needed = round(carbs_cals / 4,2)
	calories_rounded = round(calories_needed,2)
	
	values = {'cal': calories_rounded, 'pro': protein_needed, 'fat': fats_needed,
			  'carb': carbs_needed}

	return values

def calcXLoss(weight):
	calories_needed = weight * 16 - 900
	protein_needed = round(weight * 1.5,2)
	protein_cals = protein_needed * 4
	fats_cals = calories_needed * .25
	fats_needed = round(fats_cals / 9,2)
	carbs_cals = calories_needed - protein_cals - fats_cals
	carbs_needed = round(carbs_cals / 4,2)
	calories_rounded = round(calories_needed,2)
	
	values = {'cal': calories_rounded, 'pro': protein_needed, 'fat': fats_needed,
			  'carb': carbs_needed}

	return values
	
def calcXGain(weight):
	calories_needed = weight * 16 + 500
	protein_needed = round(weight * 1.5,2)
	protein_cals = protein_needed * 4
	fats_cals = calories_needed * .25
	fats_needed = round(fats_cals / 9,2)
	carbs_cals = calories_needed - protein_cals - fats_cals
	carbs_needed = round(carbs_cals / 4,2)
	calories_rounded = round(calories_needed,2)
	
	values = {'cal': calories_rounded, 'pro': protein_needed, 'fat': fats_needed,
			  'carb': carbs_needed}

	return values