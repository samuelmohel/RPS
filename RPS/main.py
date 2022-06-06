from random import randint

# list of play options
R = "Rock"
P = "Paper"
S = "Scissors"
options = ["R", "P", "S"]
computer = options[randint(0,2)]

player = False

while player == False:
#set player to True
    player = input("R, P, S?: ")
    print(f"player ({player}) : CPU ({computer})")
    if player == computer:
        print(" it is a Tie! try again")
        player = False
    elif player == 'R':
        if computer == 'P':
            print("You lose!", "Paper", "covers", "Rock")
        
        else:
            print("You win!","Rock" , "smashes", "Paper")

    elif player == 'P':
        if computer == 'S':
            print("You lose!", "Scissors", "cut", "Paper")
            
        else:
            print("You win!", "Paper", "covers", "Rock")
            
    elif player == 'S':
        if computer == 'R':
            print("You lose...", "Rock", "smashes", "scissors")
            
        else:
            print("You win!", "Scissors", "cut", "Paper")
        break
    else: 
        print("wrong entry! try again !(your entry must be in capital letter) ")
        player = False
        # computer = options[randint(0,2)]