# implementation of card game - Memory by 2ba

import simplegui
import random

global counter
a = range(8)
b = range(8)
card_deck = a+ b
random.shuffle(card_deck)
exposed = [False]*16
counter=0
# helper function to initialize globals
def new_game():
    global state, exposed
    state=0
    counter =0
    exposed = [False]*16
    random.shuffle(card_deck)
    message= "Turns=" + str(counter)
    label.set_text(str(message))

# define event handlers
def mouseclick(pos):
    global exposed
    global state
    global card_ind1
    global card_ind2
    global counter
    global message
    card_index = pos[0]//50
    if exposed[card_index]:
        pass
    else:
        if state==0:          
            exposed[card_index] = True        
            card_ind1 = card_index
            state=1
            
        elif state ==1:    
            exposed[card_index] = True
            card_ind2 = card_index              
            state =2
            
        elif state ==2:
            if card_deck[card_ind1] == card_deck[card_ind2]:
                exposed[card_ind1] = True
                exposed[card_ind2] = True 
                
            else:
                exposed[card_ind1] = False
                exposed[card_ind2] = False
            counter+=1   
            print counter
            state=1
            card_ind1 = card_index
            exposed[card_index] = True
            message= "Turns=" + str(counter)
            label.set_text(str(message))
            
       
# cards are logically 50x100 pixels in size    
def draw(canvas):  
    global i
#    pos_numbers = [20,60]
    for i in range(len(card_deck)):
        pos_x = 50*i
        if exposed[i] == True:
            canvas.draw_text(str(card_deck[i]) , (pos_x,70), 60, "White")
        else:
            canvas.draw_polygon([(pos_x, 0), ((i+1)*50, 0), ((i+1)*50,100), (pos_x, 100)], 1, 'Black')
    frame.set_canvas_background("Green")
              
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)



# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
label = frame.add_label("Turns=0")
# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
