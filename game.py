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
    def __init__(self, type):
        self.current = []
        self.count = 0

        # player vs dealer
        self.type = type


    def hit(self, card):
        self.count += Hand.value(card)
        self.current.append(card)

    def value(card):
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        card_count = [1,2,3,4,5,6,7,8,9,10,10,10,10,10]
        count_dict = dict(zip(cards,card_count))

        return count_dict[card[0]]


class Table:
    def __init__(self,players):
        self.seats = dict()

        for player in range(players):
            self.seats[f'player{player}'] = Hand('player')

        self.seats['dealer'] = Hand('dealer')

        self.deck = Deck()
    
    def deal(self):
        for i in range(2):
            for hand in self.seats.values():
                hand.hit(self.deck.draw())




class Game:
    def __init__(self, players=1):
        self.players_count = players
        self.table = Table(players)
        


        
