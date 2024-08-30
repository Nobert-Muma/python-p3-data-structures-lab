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
    pass
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    pass
    return [food for food in spicy_foods if food["heat_level"]>5]

def print_spicy_foods(spicy_foods):
    pass
    for food in spicy_foods:
        name=food["name"]
        cuisine=food["cuisine"]
        heat_level=food["heat_level"]*"🌶"
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
    # return [(food["name"]+" "+(food["cuisine"])+" "+"|"+" "+"Heat Level:"+" "+food["heat_level"]*"🌶"+"\n") for food in spicy_foods]


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    for food in spicy_foods:
        if food["cuisine"]==cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    pass
    for food in spicy_foods:
        if food["heat_level"]>5:
            name=food["name"]
            cuisine=food["cuisine"]
            heat_level=food["heat_level"]*"🌶"
            # return f"{name} ({cuisine}) | Heat Level: {heat_level}"
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    pass
    sum=0
    heat_levels=list()
    for food in spicy_foods:
        heat_level=food["heat_level"]
        heat_levels.append(heat_level)
    for level in heat_levels:
        sum+=level
    average=sum/len(heat_levels)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods
