import random
import card as cd

class Deck:
    '''Class Deck provides deck functionality, such as create deck, shuffle etc.'''

    def __init__(self):
        self.__deck = self.__populate_deck()

    def __populate_deck(self):
        '''Populate empty deck or repopulate used deck. Returns list of Card objects'''

        __card_options = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        __suit_options = ['♠', '♦', '♥', '♣']

        deck = []

        for value in __card_options:
            for suit in __suit_options:
                card = cd.Card(value, suit)
                deck.append(card)
        
        return deck
    
    def shuffle(self):
        '''Shuffles deck in-place without re-creating deck'''
        random.shuffle(self.__deck)

    def get_deck(self):
        '''Returns current state of deck'''
        return self.__deck
    
    def deal_card(self):
        '''Deals random card and removes it from deck'''
        card = self.__deck.pop()
        return card
    
    def is_deck_halfempty(self):
        '''Returns True if there are less than half of remaining cards'''
        return len(self.__deck) < len(self.__deck) / 2
        
    def __str__(self):
        '''Prints deck in format 4 Hearts, 5 Clubs etc.'''
        return 'The deck is %s' % [{card.get_card_as_string()} for card in self.__deck]        
