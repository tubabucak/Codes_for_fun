# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print "New game! The range is [0,100)"
    print "Number of guesses left: 7" 
    global number_guess
    number_guess =7
    global secret_number 
    secret_number = random.randrange(0, 100)
    # remove this when you add your code  
    
    pass


# define event handlers for control panel
def range100():
    global secret_number
    secret_number = random.randrange(0, 100)
    global number_guess
    number_guess=7
    print "New game! The range is [0,100)"
    print "Number of guesses left:", number_guess
    # button that changes the range to [0,100) and starts a new game 


    # remove this when you add your code    
    pass

def range1000():
    global secret_number
    global number_guess
    number_guess=10
    print "New game! The range is [0,1000)"
    print "Number of guesses left:", number_guess
    # button that changes the range to [0,1000) and starts a new game     
    secret_number = random.randrange(0, 1000)
    pass
    
def input_guess(guess):
        
    # main game logic goes here	
    guess = int(guess)
    print "Guess was", guess
    if secret_number < guess:
        print "Lower"
    elif secret_number > guess:
        print "Higher"
    elif secret_number == guess:
        print "Correct"
    global number_guess
    number_guess = number_guess -1
    if number_guess >= 1 and not secret_number == guess:
        print "Number of guesses left:", number_guess
    if number_guess == 0 or secret_number == guess:
        new_game()

    pass

    
# create frame

f = simplegui.create_frame("Guess the number", 200,200)

# register event handlers for control elements and start frame
f.add_input("Enter a guess", input_guess, 200)
f.add_button("Range is [0,100)",range100, 200)
f.add_button("Range is [0,1000)",range1000, 200)

# call new_game 
new_game()

f.start()
# always remember to check your completed program against the grading rubric
