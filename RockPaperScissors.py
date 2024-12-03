import random
player_action = ""
computer_action = ""
computer_point = 0
player_point = 0
rounds = 0
while rounds < 5:
    player_action = input("What do you play, rock, paper, or scissors? ")
    computer_action = random.randint(1, 3)
    if computer_action == 1:
        computer_action = "rock"
    elif computer_action == 2:
        computer_action = "paper"
    elif computer_action == 3:
        computer_action = "scissors"
    print("The computer picked " + str(computer_action))
    if player_action.lower() == "rock" and computer_action == "rock":
        print("Tie!")
        rounds = rounds + 1
    elif player_action.lower() == "rock" and computer_action == "paper":
        print("Computer got the point!")
        computer_point = computer_point + 1
        rounds = rounds + 1
    elif player_action.lower() == "rock" and computer_action == "scissors":
        print("Player got the point!")
        player_point = player_point + 1
        rounds = rounds + 1
    elif player_action.lower() == "paper" and computer_action == "rock":
        print("Player got the point!")
        player_point = player_point + 1
        rounds = rounds + 1
    elif player_action.lower() == "paper" and computer_action == "paper":
        print("Tie!")
        rounds = rounds + 1
    elif player_action.lower() == "paper" and computer_action == "scissors":
        print("Computer got the point!")
        computer_point = computer_point + 1
        rounds = rounds + 1
    elif player_action.lower() == "scissors" and computer_action == "rock":
        print("Computer got the point!")
        computer_point = computer_point + 1
        rounds = rounds + 1
    elif player_action.lower() == "scissors" and computer_action == "paper":
        print("Player got the point!")
        player_point = player_point + 1
        rounds = rounds + 1
    elif player_action.lower() == "scissors" and computer_action == "scissors":
        print("Tie!")
        rounds = rounds + 1
    else:
        print("Redo that round!")
if player_point > computer_point:
    print("Player wins it all!!!!!")
elif computer_point > player_point:
    print("Computer wins it all!!!!!")