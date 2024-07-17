#Rock Paper Scissor

# print(type(dict_inputs))
import random  #Googled how to use random, Thanks to w3schools.
computer_chocies = ["Rock", "Paper", "Scissor"]
computer_input = random.choice(computer_chocies)
r = "Rock"
p = "Paper"
s = "Scissor"
user_input = input("Rock \nPaper \nScissor \nEnter one of the choices given above: ").capitalize()

#Defines all the ties
if computer_input==user_input:
    print("Its a tie.")
#Rock cases.
#Rock vs Paper cases
elif computer_input==r and user_input==p:
    print("You won!")
elif computer_input==p and user_input==r:
    print("Computer won!")
#Rock vs Scissor
elif computer_input==r and user_input==s:
    print("Computer won!")
elif computer_input==s and user_input==r:
    print("You won!")

# Scissor cases
# Scissor vs paper
elif computer_input==p and computer_input==s:
    print("You Won!")
elif computer_input==s and computer_input==p:
    print("Computer Won!")
#Scissor vs Rock
elif computer_input==s and computer_input==r:
    print("You won!")
elif computer_input==r and computer_input==s:
    print("Computer won!")

# Paper Cases
# Paper Vs Rock
elif computer_input==p and user_input==r:
    print("Computer Won!")
elif computer_input==p and user_input==r:
    print("You won!")
#Paper Vs Scissors
elif computer_input==p and user_input==s:
    print("You won!")
elif computer_input==s and user_input==p:
    print("Computer Won")
else:
    print("Enter a valid choice")
# remove the "#" or un-comment it to see the computer choice once the game is completed.
# print(f"Computer choosed {computer_input}")
