import random


class Deck:
    def __init__(self, deck_size=1):
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['D', 'C','H', 'S']
        self.full_deck = [(card,suit) for card in deck_size * cards for suit in suits]
        self.current = self.full_deck


    #shuffle all cards in the current deck
    def shuffle(self):
        random.shuffle(self.current)

    # draws last card from current deck
    def draw(self):
        return self.current.pop()


class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.current = []
        self.count = 0

        #tracks lower count in case of 'Ace' card
        self.alt_count = 0

    def hit(self, deck):

        '''
        1. draws card.
        2. if 'A' is drawn and count <= 10, 'A' has two values.
        2. if alt count is used, add card value to count and alt count
            a. if main count is bust, alt count becomes main count. 
            b. if neither is bust, use both
        
        '''

        card = deck.draw()
        
        # calculating total hand count
        if card[0] == 'A' and self.count <= 10:   
            if self.dealer:
                # if dealer's hand and count is less than 10, Ace treated as 11; otherwise treated as one
                self.count += 11
            else: 
                # if main count is <= 10, alt_count is count + 11. 
                # If count is 11 or higher, Ace as 11 would bust
                self.alt_count = self.count + 11
                self.count += Hand.value(card)
                
        elif self.alt_count:
            # if alt count exist, add card value to both count and alt count
            # Ace treated as 1 if self.count >= 1.  
            self.alt_count += Hand.value(card)
            self.count += Hand.value(card)

        else:
            # if not any of conditions above, add card value to count
            self.count += Hand.value(card)
        
        # check hand count
        if self.alt_count > 21:
            self.alt_count = 0
        

        
        

        self.current.append(card)

    def value(card):
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        card_count = [1,2,3,4,5,6,7,8,9,10,10,10,10,10]
        count_dict = dict(zip(cards,card_count))

        return count_dict[card[0]]

    def clear(self):
        self.current = []
        self.count = 0

    def display(self):
        if self.alt_count:
            print(f"hand: {self.current}, count: {self.count},({self.alt_count})")
        else:
            print(f"hand: {self.current}, count: {self.count}")



class Player:
    def __init__(self,name):

        # player vs dealer
        self.name = name
        self.type = 'player'
        self.hand = Hand()
    
    def hit(self, deck):
        self.hand.hit(deck)

    def display(self):
        print(f"player:{self.name}") 
        self.hand.display()






class Dealer(Player):
      def __init__(self):

        # player vs dealer
        self.name = 'Dealer'
        self.type = 'dealer'
        self.hand = Hand(dealer=True)




class Table:
    def __init__(self,players):
        self.seats = []

        for player in range(players):
            self.seats.append(Player(f"Player {player+1}"))
        
        self.seats.append(Dealer())

        self.deck = Deck()


    def deal(self):
        print("-----Dealing Cards-----")
        self.clear()
        self.deck.shuffle()
        for i in range(2):
            for player in self.seats:
                player.hand.hit(self.deck)
                player.status = 'play'
        self.display()
        
    def action(self):
        print('-----Starting Turn-----')
        for player in self.seats:
            while player.status == 'play':
                player.display()
                action = input("Hit or Stand")
                if action.lower() == 'hit':
                    player.hit(self.deck)
                    player.display()
                    if player.hand.count > 21:
                        print('BUST!')
                        player.status = 'bust'
                elif action.lower() == 'stand':
                    player.status = 'stand'


    # clear hands in table
    def clear(self):
        for player in self.seats:
            player.hand.clear()

    # displays all hands and counts for each player
    def display(self):
        for player in self.seats:
            player.display()

    

    



class Game:
    def __init__(self, players=1):
        self.table = Table(players)

    def run_game(self):
        replay = True
        while replay:
            self.table.deal()
            self.table.action()

            replay_q = input('========replay? (y/n)=========')

            replay = replay_q == 'y'



        


        
