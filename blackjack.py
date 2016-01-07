http://www.codeskulptor.org/#user40_s7M0I7Poea_1.py

       
# Mini-project #6 - Blackjack by 2ba :)

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or deal?"
score = 0
play_deck=[]
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
   
       
# define hand class        
class Hand:
    def __init__(self):
        self.hand =[] # create Hand object
            
    def __str__(self): 
        ans = "Hand contains"
        for i in range(len(self.hand)):
            ans += " "+ str(self.hand[i])
        return ans
 
    def add_card(self, card):
        self.card = card
        self.hand.append(card)
            # add a card object to a hand
        return self.hand
    
 
    def get_value(self):
        self_value = 0
        for i in self.hand:
            self_value += VALUES.get(i.get_rank())
            if i.get_rank()== 'A' and self_value + 10 <= 21:
                self_value +=10
        return self_value
   
    def draw(self, canvas, pos):
        for card in self.hand:  
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(Card.get_rank(card)), 
               CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(Card.get_suit(card)))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [(pos[0]+36)*(self.hand.index(card)) + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], 
                    CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [(pos[0]+36)*0 + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
   
# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for sui in SUITS:
            for ran in RANKS:
                self.deck.append(Card(str(sui),str(ran)))# create a Deck object
                    
            
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)   # use random.shuffle()

    def deal_card(self):
        random_deck = random.choice(self.deck)
        return random_deck
        self.deck.remove(random_deck)
    
    def __str__(self):
            # return a string representing the deck
        ans = "Deck contains"
        for i in range(len(self.deck)):
            ans += " "+ str(self.deck[i])
        return ans



#define event handlers for buttons
def deal():
    global outcome, in_play, card1_player, card2_player, card1_dealer, card2_dealer, player, dealer, my_deck, score
    
    if in_play==True:
        score= score-1
        outcome = "You lost the round. A new deal?"
        in_play= False
    else:    
        outcome= "Hit or deal?"
        my_deck= Deck()
        my_deck.shuffle()
        card1_player = Deck.deal_card(my_deck)
        card2_player = Deck.deal_card(my_deck)
        card1_dealer = Deck.deal_card(my_deck)
        card2_dealer = Deck.deal_card(my_deck)
        player= Hand()
        dealer= Hand()
        player.add_card(card1_player)
        player.add_card(card2_player)
        dealer.add_card(card1_dealer)
        dealer.add_card(card2_dealer)
        # your code goes here   
        in_play = True

def hit():
          
    # if the hand is in play, hit the player
    
    # if busted, assign a message to outcome, update in_play and score  
    global player, my_deck, score, in_play, outcome
    outcome ="Hit or stand ?"
    if player.get_value() <= 21 and in_play == True:
        player.add_card(Deck.deal_card(my_deck))
    elif player.get_value() >21:
        outcome = "You have busted! A new deal?"
        score = score-1
        in_play=False

def stand():
    global in_play, dealer, player, my_deck, outcome, score
    if player.get_value() > 21:
        outcome= "Sorry, you have busted! A new deal?"
        score = score-1
        in_play= False
    else:
        while dealer.get_value() <=17:
            in_play= True
            dealer.add_card(Deck.deal_card(my_deck))
        if dealer.get_value() > 21:
            in_play = False
            outcome= "Dealer Busted! A new deal?"
            score = score +1
            print score
        elif dealer.get_value() >= player.get_value():
            outcome= "Dealer wins! A new deal?"
            score = score-1
            in_play= False
        else:
            outcome ="You won! A new deal?"
            score = score+1
            in_play= False
    return outcome
            

# draw handler    
def draw(canvas):
    global outcome, player, in_play, back_loc,score
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
   # card.draw(canvas, [300, 300])
    canvas.draw_text("Player", (50, 420), 30, 'Red')
    canvas.draw_text("Dealer", (50, 120), 30, 'Blue')
    canvas.draw_text(outcome, (100, 350), 30, 'Black')
    canvas.draw_text("Score = " + str(score), (300, 120), 30, 'Black')
    player.draw(canvas,[60, 450])
    #dealer.draw(canvas,[50, 150])
    canvas.draw_text("Blackjack", (50, 60), 40, 'Black')
    if in_play==True:
        dealer.draw(canvas,[60, 150])
        dealer.draw_back(canvas,[60, 150])
        
    else:
        dealer.draw(canvas,[50, 150])
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric


# remember to review the gradic rubric
    

