speding_amount = int(input("How many expenses did you have today? "))
count = 0
expenses_list = []

while count + 1 <= speding_amount:
    expense = float(input("Type the {}th expense you did today: ".format(count + 1)))

    expenses_list.append(expense)

    count += 1

total_value = 0
for expense in expenses_list:
    total_value += expense

print("You spent a total of R${}".format(total_value))
