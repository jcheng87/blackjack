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
    def __init__(self):
        self.current = []
        self.count = 0

    def hit(self, deck):
        card = deck.draw()
        self.count += Hand.value(card)
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
        print(f"hand: {self.current}, count: {self.count}")



class Player:
    def __init__(self):

        # player vs dealer
        self.type = 'player'
        self.hand = Hand()
    
    def hit(self, deck):
        self.hand.hit(deck)

    def display(self):
         print(f"player:{self.type}") 
         self.hand.display()






class Dealer(Player):
      def __init__(self):

        # player vs dealer
        self.type = 'dealer'
        self.hand = Hand()




class Table:
    def __init__(self,players):
        self.seats = []

        for player in range(players):
            self.seats.append(Player())
        
        self.seats.append(Dealer())

        self.deck = Deck()


    def deal(self):
        self.clear()
        self.deck.shuffle()
        for i in range(2):
            for player in self.seats:
                player.hand.hit(self.deck)
                player.status = 'play'
        self.display()
        
    def action(self):
        for player in self.seats:
            while player.status == 'play':
                player.display()
                action = input("Hit or Stand")
                if action.lower() == 'hit':
                    player.hit(self.deck)
                    if player.hand.count > 21:
                        print('BUST!')
                        player.status = 'bust'
                elif action.lower() == 'stand':
                    player.status = 'stand'



    def clear(self):
        for player in self.seats:
            player.hand.clear()

    def display(self):
        for player in self.seats:
            player.display()

    

    



class Game:
    def __init__(self, players=1):
        self.players_count = players
        self.table = Table(players)
        


        
