from Computer import Computer
from Human import Human


class Screen:
    def __init__(self):
        pass

    def show_message(self, message):
        '''Prints message on console'''
        print(message)

    def get_input(self, message):
        return input(f"{message} ")
    
    def get_hands_printable(self, player, is_cpu_turn):
        '''Prints hand'''
        if type(player) == Human:
            result = []
            for card in player.get_hand():
                result.append(card.get_card_as_string())
            return ", ".join(result)
        elif type(player) == Computer:
            if is_cpu_turn:
                result = []
                for card in player.get_hand():
                    result.append(card.get_card_as_string())
                return ", ".join(result)
            else:
                return player.get_hand()[0].get_card_as_string()
