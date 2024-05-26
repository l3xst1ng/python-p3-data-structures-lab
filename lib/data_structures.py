spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # empty list to store the names of spicy foods
    names = []
    for food in spicy_foods:

        names.append(food["name"])
    return names

def get_spiciest_foods(spicy_foods):
    # empty list to store the spiciest foods
    spiciest_foods = []
    
    for food in spicy_foods:
        # Checking if the heat_level of the food is greater than 5
        if food["heat_level"] > 5:
            #  append the food to the spiciest_foods list if the heat_level is greater than 5
            spiciest_foods.append(food)
    # Return the list of spiciest foods
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    
    for food in spicy_foods:
        #  string of chili pepper emojis based on the food heat_level 
        heat_level_emoji = "🌶" * food["heat_level"]
        # Printing the name, cuisine, and heat level of the food
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):

    for food in spicy_foods:
        # Checking if the cuisine of the food matches the given cuisine
        if food["cuisine"] == cuisine:
            
            return food

def print_spiciest_foods(spicy_foods):
    # Getting the list of spiciest foods by calling the get_spiciest_foods function
    spiciest_foods = get_spiciest_foods(spicy_foods)
    # Printing the spiciest foods by calling the print_spicy_foods function
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):

    total_heat_level = 0
    # Looping through each food in the spicy_foods list
    for food in spicy_foods:
        # Adding the heat_level of the food to the total_heat_level
        total_heat_level += food["heat_level"]

    average_heat_level = total_heat_level / len(spicy_foods)

    return int(average_heat_level)

def create_spicy_food(spicy_foods, spicy_food):
    
    spicy_foods.append(spicy_food)
    
    return spicy_foods
