import random
from colorama import Fore, Back, Style


class Game:

    def __init__(self, comp_wins=0, player_wins=0, games_played=0):

        self.comp_wins = comp_wins
        self.player_wins = player_wins
        self.games_played = games_played
        self.user_input = None
        self.computer_choose = None

    def get_user_input(self):  # user input

        user_input = input(
            'please choose\n  rock\n  paper\n  scissors\n').lower().strip()
        if user_input in ['rock', 'r']:
            self.user_input = 'rock'
        elif user_input in ['paper', 'p']:
            self.user_input = 'paper'
        elif user_input in ['scissors', 's']:
            self.user_input = 'scissors'
        else:
            print('You didn’t choose a option, please try again.')

    def get_computer_input(self):
        computer_choose = random.randint(1, 3)
        if computer_choose == 1:
            self.computer_choose = 'rock'
        elif computer_choose == 2:
            self.computer_choose = 'paper'
        else:
            self.computer_choose = 'scissors'

    def display_match_results(self):
        """
        Displays match results.
        Adds match results.
        """
        print("")
        print(Fore.GREEN + "Player wins: " + str(self.player_wins))
        print(Fore.RED + "Computer wins: " + str(self.comp_wins))
        print("")

    def winner(self):
        self.games_played += 1
        if self.user_input == "rock":
            if self.computer_choose == "rock":
                print(
                    "You chose rock. The computer chose rock too. Congrats, you tied.")# noqa

            elif self.computer_choose == "paper":
                print("You chose rock. The computer chose paper. you lose.")
                self.comp_wins += 1

            elif self.computer_choose == "scissors":
                print("You chose rock. The computer chose scissors. You win!")
                self.player_wins += 1

        elif self.user_input == "paper":

            if self.computer_choose == "rock":
                print(
                    "You chose paper. The computer chose rock. You win!.")
                self.player_wins += 1

            elif self.computer_choose == "paper":
                print(
                    "You chose paper. The computer chose paper too. Congrats, you tied.")# noqa

            elif self.computer_choose == "scissors":
                print(
                    "You chose paper. The computer chose scissors. you lose.")
                self.comp_wins += 1

        elif self.user_input == "scissors":

            if self.computer_choose == "rock":
                print(
                    "You chose scissors. The computer chose rock. you lose.")
                self.comp_wins += 1

            elif self.computer_choose == "paper":
                print(
                    "You chose scissors. The computer chose paper. You win!.")
                self.player_wins += 1

            elif self.computer_choose == "scissors":
                print(
                    "You chose scissors. The computer chose scissors too. Congrats, you tied.")# noqa

    def play_again(self):
        """
        Asks user if they want to play again by entering Y or N
        """
        play_again_option = input(
            f'Would you like to play again? (Y/N)').strip().upper()
        print('\n')
        if play_again_option == 'Y':
            main()
        elif play_again_option == 'N':
            self.games_played += 1
            print('Thanks for playing! \n')
        else:
            print('Invalid choice \n')
            self.play_again()

    def play(self):

        self.get_user_input()
        self.get_computer_input()
        self.winner()
        self.display_match_results()
        self.play_again()


def main():

    game = Game()

    while True:

        return game.play()
