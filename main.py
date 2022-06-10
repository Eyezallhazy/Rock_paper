import random

def user_selection():
    valid_character = ["R","P","S"]
    print("Enter a selection")
    print("R for Rock")
    print("P for Paper")
    print("S for Scissor")
    print()
    user_entry = input("Enter choice: ").upper()

    while user_entry not in valid_character:
        user_entry = input("Enter valid choice: ").upper()

    return user_entry

def computer_selection():
    valid_character =["R","P","S"]
    computer_choice = random.choice(valid_character)

    return computer_choice

def check_win(first_option, second_option):
    if first_option == "R" and second_option == "S":
        return True
    elif first_option == "P" and second_option == "R":
        return True
    elif first_option == "S" and second_option == "P":
        return True
    else:
        return False

def start_game(user_select, comp_select):
    # 0 represents a draw, 1 represents a win for the user, 2 represents a win for the computer
    if user_select == comp_select:
        return 0
    elif check_win(user_select, comp_select):
        return 1
    else: 
        return 2

print("Getting the users input\n\n")
user_select = user_selection()
print(f"You have entered: {user_select}")
print("\nGetting computer choice")
comp_select = computer_selection()
print(f"Computer entered {comp_select}")

# play the game.
begin_game = start_game(user_select, comp_select)

while begin_game == 0:
    print("It's a draw, you have to keep on playing")
    print("Getting the users input\n\n")
    user_select = user_selection()
    print(f"You have entered: {user_select}")
    print("\nGetting computer choice")
    comp_select = computer_selection()
    print(f"Computer entered {comp_select}")

    # play the game.
    begin_game = start_game(user_select, comp_select)

if begin_game == 1:
    print("Congratulations!, user won (YOU WIN, HURRAY!)")
else:
    print("Oops!, Sorry, you lose. COMPUTER WINS, try again next time")



# when you have Rock Paper -> 
