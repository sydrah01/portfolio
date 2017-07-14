import random

Salads = ["Ceasar", "Blue Cheese", "chicken", "plain"]
Meals = ["cheeseburger with fries", "Pizza", "Steak", "Rice and Kebab", "Choice of Taco", "Soup of choice"]
Dessert = ["Icecream", "Brownie", "cookies"]

for item in Salads:
	print(item)

num_items = len(Salads)
for item in range(num_items):
	print("salad is " + Salads[item])
	print("meal item is " + Meals[item])
	print("desert is " + Dessert[item])