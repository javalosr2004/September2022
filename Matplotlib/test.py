dict = {'Protein': 60, 'Fats':30, 'Carbs' : 40}

sorted_keys = sorted(dict, key=dict.get)
print(sorted_keys)