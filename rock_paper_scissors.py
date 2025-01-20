import random 

player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
computer_choice = random.choice(["rock", "paper", "scissors"])

print(f"Computer chose {computer_choice}")
 
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock":
    if computer_choice == "paper":
        print("You lose!")
    else:
        print("You win!")
elif player_choice == "paper":
    if computer_choice == "scissors":
        print("You lose!")
    else:
        print("You win!")
elif player_choice == "scissors":
    if computer_choice == "rock":
        print("You lose!")
    else:
        print("You win!")
else:
    print("Invalid choice. Please enter rock, paper, or scissors.")


