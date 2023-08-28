from computer import Computer
from human import Human


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
    
    def add_heavy_line(self):
        self.show_message("=====================")

    def add_single_line(self):
        self.show_message("----")

