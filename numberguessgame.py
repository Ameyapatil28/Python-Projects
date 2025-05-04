import random

a = 0

def game():
    global a
    random_number = random.randint(1, 100)
    number = -1  

    while number != random_number:
        user_input = input("Enter your guess: ")

        if user_input.isdigit():  # ensures input is a positive integer
            number = int(user_input)

            if number > random_number:
                print("Enter a smaller number")
                a += 1
            elif number < random_number:
                print("Enter a bigger number")
                a += 1
        else:
            print("Please enter a valid positive integer.")

    print(f"You guessed the correct number {random_number} in {a} guesses.")

game()
