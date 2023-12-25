import random

game_list = ["rock", "paper", "scissor"]

while True:
    your_count = 0
    computer_count =0

    player_choice = int(input('''
    Do you want to start the game?
    1 yes | start
    2 no | exit
    '''))
    if player_choice == 1:
        for game_round in range(1, 6):
            game_options = int(input('''
            1  rock
            2  paper
            3  scissor
            '''))
            if game_options == 1:
                your_choice = "rock"
            elif game_options == 2:
                your_choice = "paper"
            elif player_choice == 3:
                your_choice = "scissor"
            computer_choice = random.choice(game_list)

            if computer_choice == your_choice:
                print("computer choice: ", computer_choice)
                print("your choice: ", your_choice)
                print("Game draw")
                your_count += 1
                computer_count += 1
            elif ((your_choice == "paper" and computer_choice == "rock") or
                  (your_choice == "scissor" and computer_choice == "paper") or
                  (your_choice == "rock" and computer_choice == "scissor")):
                print("computer choice: ", computer_choice)
                print("your choice: ", your_choice)
                print("You win")
                your_count += 1
            else:
                print("computer choice: ", computer_choice)
                print("your choice: ", your_choice)
                print("Computer won")
                computer_count += 1

        if your_count == computer_count:
            print("Final game draw.....")
            print("your score: ", your_count)
            print("computer score: ", computer_count)
        elif your_count > computer_count:
            print("You won the game.....")
            print("your score: ", your_count)
            print("computer score: ", computer_count)
        else:
            print("computer won the game.....")
            print("your score: ", your_count)
            print("computer score: ", computer_count)
    else:
        break
