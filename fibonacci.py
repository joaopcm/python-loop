user_input = int(input("Type your choice: "))
current_fibonacci_number = 0
fibonacci_history = [1]
user_got_it_right = False

while user_input >= current_fibonacci_number and user_input != current_fibonacci_number:
    current_fibonacci_number = (fibonacci_history[-2] if len(fibonacci_history) != 1 else 0) + fibonacci_history[-1]
    fibonacci_history.append(current_fibonacci_number)

    user_got_it_right = user_input == current_fibonacci_number

print("You got it {}!".format("right" if user_got_it_right else "wrong"))
