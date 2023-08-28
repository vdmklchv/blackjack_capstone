import Screen as sc
from Deck import Deck
from Human import Human
from Computer import Computer
from Processor import Processor
from art import art

class Game:
    deck = Deck()
    screen = sc.Screen()
    pc = Processor()    

    def __init__(self):
        pass

    def __should_start_new_game(self):
        '''Greets user and returns user choice to start game or not'''
        start_game = self.screen.get_input("Do you want to play blackjack? Print y to start, anything else to stop: ")

        return start_game == "y"
    
    def __show_hands(self, human, computer, is_cpu_turn):
        self.screen.show_message(f"{human.get_name()}'s hand is [{self.screen.get_hands_printable(human, is_cpu_turn)}]")
        self.screen.show_message(f"Your hand is {self.pc.calculate_score(human)} points.")
        self.screen.show_message(f"{computer.get_name()}'s hand is [{self.screen.get_hands_printable(computer, is_cpu_turn)}]")
        
    
    def __get_username(self):
        '''Asks user name from user input'''
        return self.screen.get_input("What is your name?")
    
    def __create_player(self, type, name = "Computer"):
        '''Creates player of chosen type. Available types are human and computer, other arguments will return None'''
        if (type == "human"):
            return Human(name)
        elif (type == "computer"):
            return Computer()
        
    def __cpu_play(self, human_player, computer_player, is_cpu_turn = True):
        '''CPU moving (auto draw if less than 17). Stand if >= 17'''
        while self.pc.calculate_score(computer_player) < 17:
            self.screen.show_message("Computer takes a new card...")
            computer_player.add_card(self.deck.deal_card())
            self.__show_hands(human_player, computer_player, is_cpu_turn)
        self.screen.show_message("Computer stands.")
        self.screen.show_message(f"Computer hand is {self.pc.calculate_score(computer_player)}")


    def play_game(self):
        '''Function to start game, contains game logic'''
        self.screen.show_message(art)
        ## Create players
        user_name = self.__get_username()
        human_player = self.__create_player('human', user_name)
        computer_player = self.__create_player('computer')

        assert human_player is not None
        assert computer_player is not None

        is_game_on = self.__should_start_new_game()

        ## Main game logic
        while is_game_on:
            # clear hands on each game
            human_player.clear_hand()
            computer_player.clear_hand()

            self.screen.show_message("The Blackjack Game begins!")
            if self.deck.is_deck_halfempty():
                self.screen.show_message("Replenishing deck...")
                self.deck = Deck()

            #shuffle deck
            self.deck.shuffle()
            # deal cards
          
            human_player.add_card(self.deck.deal_card())
            human_player.add_card(self.deck.deal_card())

            computer_player.add_card(self.deck.deal_card())
            computer_player.add_card(self.deck.deal_card())

            # show 1 card of cpu and both cards of Player
            self.screen.show_message(f"Your current score is {human_player.get_score()}")
            self.__show_hands(human_player, computer_player, False)
            

            # ask player to deal
            needs_card = "y"
            human_is_bust = False
            cpu_is_bust = False
            while needs_card == "y":
                if self.screen.get_input("Would you like another card? y for yes, any button for no: ") == "y":
                    human_player.add_card(self.deck.deal_card())
                    self.__show_hands(human_player, computer_player, False)
                    if self.pc.is_bust(human_player):
                        self.screen.show_message(f"You bust! Your score is {self.pc.calculate_score(human_player)}")
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
                    winner = self.pc.get_winner(human_player, computer_player)
           
                    if winner == None:
                        self.screen.show_message("It's a tie!")
                    else:
                        self.__show_hands(human_player, computer_player,True)
                        self.screen.show_message(f"Computer hand is {self.pc.calculate_score(computer_player)}")
                        self.screen.show_message(f"{winner.get_name()} wins!")
                        winner.update_score()
                else:
                    self.screen.show_message(f"Computer bust! His score is {self.pc.calculate_score(computer_player)}. You win!")
                    human_player.update_score()

            # ask if user wants to play again
            is_game_on = self.__should_start_new_game()
        
        self.screen.show_message("Thanks for playing! Goodbye!")
        
        