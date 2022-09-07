from dataclasses import dataclass


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt



CALORIE_GOAL_LIMIT = 3000 #kcal
PROTEIN_GOAL = 180 #g
FAT_GOAL = 80 #g
CARBS_GOAL = 300 #g

today = []

@dataclass
class Food:
    name : str
    calories : int
    protein : int
    fats: int
    carbs : int


done = False

while not done:
    print('''\n\n\n\n\n\n\n\n\n\n\n\n\n
    (1) Add a new food
    (2) Visualize progress
    (q) Quit
    ''')

    user_choice = input('Choose an option:  ')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    if user_choice == '1':
        print('Adding a new food!')
        name = input('Name: ')
        calories = int(input('Calories: '))
        protein = int(input('Protein: '))
        fats = int(input('Fats: '))
        carbs = int(input('Carbs: '))
        food = Food(name, calories, protein, fats, carbs)
        today.append(food)

        print('\nSuccesfully added!')
    elif user_choice == '2':
        calorie_sum = sum(food.calories for food in today)
        macro_dict = {}

        macro_dict['Protein'] = sum(food.protein for food in today)
        macro_dict['Fats'] = sum(food.fats for food in today)
        macro_dict['Carbs'] = sum(food.carbs for food in today)
        
        
        keySorted = sorted(macro_dict, key = macro_dict.get) #sorts the values in the macro dictionary
        macroSorted = [macro_dict[x] for x in keySorted] #creates a sorted value pair in relation to this new sort
        myexplode = [0 for x in range(len(keySorted) -1)] #will cause the highest valued macro to be set apart from the others
        myexplode.append(0.2)

        pie_values = np.array(macroSorted)

        plt.pie(pie_values, explode = myexplode, autopct='%1.1f%%')
        plt.legend(keySorted)
        plt.show()
    else:
        done = True
        

