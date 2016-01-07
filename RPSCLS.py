# Rock-paper-scissors-lizard-Spock Mini Project
# here is the link : http://www.codeskulptor.org/#user40_GvFpkWRDk2rMZ0I.py
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
        name_num = 0
    elif name == "Spock":
        name_num = 1
    elif name == "paper":
        name_num = 2
    elif name == "lizard":
        name_num = 3
    elif name == "scissors":
        name_num = 4
    else:
        print "It is not an appropriate name for playing game"
    return name_num
    
def number_to_name(number):
    if number == 0:
        num_name = "rock"
    elif number == 1:
        num_name = "Spock"   
    elif number == 2:
        num_name = "paper"
    elif number == 3:
        num_name = "lizard"
    elif number == 4:
        num_name = "scissors"
    else:
        print "It is not an appropriate number for playing game"
    return num_name

def rpsls(player_choice): 
    import random

    # print a blank line to separate consecutive games
    print
    # print out the message for the player's choice
    print "Player chooses", player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    
    print "Computer chooses", comp_choice
    
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if difference == 1 or difference == 2:
        print "Computer wins!"
    elif difference == 3 or difference == 4:
        print "Player wins!"
    else:
        print "Player and computer tie!"
        
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


