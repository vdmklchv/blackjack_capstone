import Screen as sc
from Deck import Deck
from Human import Human
from Computer import Computer
from Processor import Processor

screen = sc.Screen()
deck = Deck()
pc = Processor()

class Game:
    def __init__(self):
        pass

    def __should_start_new_game(self):
        '''Greets user and returns user choice to start game or not'''
        start_game = screen.get_input("Do you want to play blackjack? Print y to start, anything else to stop: ")

        return start_game == "y"
    
    def __show_hands(self, human, computer, is_cpu_turn):
        screen.show_message(f"{human.get_name()}'s hand is [{screen.get_hands_printable(human, is_cpu_turn)}]")
        screen.show_message(f"Your hand is {pc.calculate_score(human)} points.")
        screen.show_message(f"{computer.get_name()}'s hand is [{screen.get_hands_printable(computer, is_cpu_turn)}]")
        
    
    def __get_username(self):
        '''Asks user name from user input'''
        return screen.get_input("What is your name?")
    
    def __create_player(self, type, name = "Computer"):
        '''Creates player of chosen type. Available types are human and computer, other arguments will return None'''
        if (type == "human"):
            return Human(name)
        elif (type == "computer"):
            return Computer()
        
    def __cpu_play(self, human_player, computer_player, is_cpu_turn = True):
        '''CPU moving (auto draw if less than 17). Stand if >= 17'''
        while pc.calculate_score(computer_player) < 17:
            screen.show_message("Computer takes a new card...")
            computer_player.add_card(deck.deal_card())
            self.__show_hands(human_player, computer_player, is_cpu_turn)
        screen.show_message("Computer stands.")
        screen.show_message(f"Computer hand is {pc.calculate_score(computer_player)}")


    def play_game(self):
        '''Function to start game, contains game logic'''
        ## Create players
        user_name = self.__get_username()
        human_player = self.__create_player('human', user_name)
        computer_player = self.__create_player('computer')

        assert human_player is not None
        assert computer_player is not None

        is_game_on = self.__should_start_new_game()

        ## Main game logic
        while is_game_on:
            screen.show_message("The Blackjack Game begins!")
            #shuffle deck
            deck.shuffle()
            # deal cards
          
            human_player.add_card(deck.deal_card())
            human_player.add_card(deck.deal_card())

            computer_player.add_card(deck.deal_card())
            computer_player.add_card(deck.deal_card())

            # show 1 card of cpu and both cards of Player
            screen.show_message(f"Your current score is {human_player.get_score()}")
            self.__show_hands(human_player, computer_player, False)
            

            # ask player to deal
            needs_card = "y"
            human_is_bust = False
            cpu_is_bust = False
            while needs_card == "y":
                if screen.get_input("Would you like another card? y for yes, any button for no: ") == "y":
                    human_player.add_card(deck.deal_card())
                    self.__show_hands(human_player, computer_player, False)
                    if pc.is_bust(human_player):
                        screen.show_message(f"You bust! Your score is {pc.calculate_score(human_player)}")
                        computer_player.update_score()
                        human_is_bust = True
                        break
                else:
                    needs_card = "n"
            
            if not human_is_bust:
                self.__show_hands(human_player, computer_player, False)
            
                # create logic for cpu to auto play
                self.__cpu_play(human_player, computer_player, True)

                if not cpu_is_bust:
                    # compare results
                    winner = pc.get_winner(human_player, computer_player)
           
                    if winner == None:
                        screen.show_message("It's a tie!")
                    else:
                        self.__show_hands(human_player, computer_player,True)
                        screen.show_message(f"Computer hand is {pc.calculate_score(computer_player)}")
                        screen.show_message(f"{winner.get_name()} wins!")
                        winner.update_score()
                else:
                    screen.show_message(f"Computer bust! His score is {pc.calculate_score(computer_player)}. You win!")
                    human_player.update_score()
            # show winner

            # show score

            # ask if user wants to play again
            is_game_on = self.__should_start_new_game()
        
        screen.show_message("Thanks for playing! Goodbye!")
        
        