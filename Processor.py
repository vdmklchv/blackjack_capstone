class Processor:

    def __init__(self):
        self.__score_system = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11
    }


    def calculate_score(self, player):
        hand = player.get_hand()
        has_ace = False
        total = 0
        for card in hand:
            if card.get_value() == "A":
                has_ace = True
            total += self.__score_system[card.get_value()]
        
        if total > 21 and has_ace:
            total -=10

        return total

    
    def get_winner(self, human, computer):
        '''returns object of winner, None if tie'''
        human_score = self.calculate_score(human)
        computer_score = self.calculate_score(computer)

        if human_score > computer_score:
            return human
        elif computer_score > human_score:
            return computer
        else:
            return None
        
    def is_bust(self, player):
        '''Checks if player has more than 21'''
        return self.calculate_score(player) > 21
    
    def hand_is_blackjack(self, player):
        '''Checks if dealt hand is blackjack and returns true or false'''
        score = self.calculate_score(player)
        return score == 21
