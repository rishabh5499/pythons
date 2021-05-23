import random

actions = ["Rock", "Paper", "Scissor"]
Upoint=0
Cpoint=0

print("Welcome to the game, enter Exit to quit")
while True:
    print("\n".join(map(str, actions)))
    user = input("Enter your move from the list: ");
    
    if(user == "Exit"):
        print("Your Points: ", Upoint, "Computer's Points: ", Cpoint)
        if Upoint > Cpoint:
            print("You won by ", Upoint-Cpoint, " points")
        elif Cpoint < Upoint:
            print("Computer won by ", Cpoint-Upoint, " points")
        else:
            print("Its a tie")
        break
        
    computer = random.choice(actions)
    print("Computer's Choice: ", computer, "\n")
    
    if user == computer:
        print("Thats a tie")
    elif user == "Rock":
        if computer == "Paper":
            print("Computer got a point")
            Cpoint+=1
        else:
            print("You got a point")
            Upoint+=1
    elif user == "Paper":
        if computer == "Scissor":
            print("Computer got a point")
            Cpoint+=1
        else:
            print("You got a point")
            Upoint+=1
    elif user == "Scissor":
        if computer == "Rock":
            print("Computer got a point")
            Cpoint+=1
        else:
            print("You got a point")
            Upoint+=1