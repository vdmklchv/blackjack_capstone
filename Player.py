class Player:
    def __init__(self, name, type):
        self.__score = 0
        self.__name = name
        self.__hand = []
        self.type = type
    
    def get_name(self):
        '''Returns name of player'''
        return self.__name
    
    def get_hand(self):
        '''Shows full player hand'''
        return self.__hand
    
    def get_score(self):
        return self.__score
    
    def update_score(self):
        self.__score += 1

    def add_card(self, card):
        '''Adds card object to players hand'''
        self.__hand.append(card)

    def clear_hand(self):
        self.__hand = []

    
    
