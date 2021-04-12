ingested_food = int(input("How many lunches have you ate today? "))
count = 0
ingested_food_list = []

while count + 1 <= ingested_food:
    food = input("Type the {}th food you ingested today: ".format(count + 1))
    calories = float(input("Type how many calories the food you ate today had: "))

    ingested_food_list.append({"food": food, "calories": calories})

    count += 1

total_calories = 0
for food in ingested_food_list:
    total_calories += food['calories']

print("You have ingested {} calories today!".format(total_calories))
