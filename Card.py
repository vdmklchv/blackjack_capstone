class Card:

    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suit

    def get_value(self):
        return self.__value
    
    def get_suit(self):
        return self.__suit
    
    def get_card_as_string(self):
        return f"{self.get_value()} {self.get_suit()}"

    
    # add number of times card was dealt (???)





    