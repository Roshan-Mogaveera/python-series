import random
choices = ["rock", "paper", "scissor"]
computer_choice = random.choice(choices)
while True:
    user_choice = input("Enter your choice ")
    if user_choice not in choices:
        print("Invalid choice ")
        break
    else:
        print(f"Computer choice is {computer_choice}")
    if user_choice == computer_choice :
        print("Its a draw")
    elif (user_choice == "rock" and computer_choice == "scissor") or (user_choice == "scissor" and computer_choice == "paper") or (user_choice == "scissor" and computer_choice == "rock"):
        print("You won the game ")
    else:
        print("Computer won the game ")