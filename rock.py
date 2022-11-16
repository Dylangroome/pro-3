import random


class Game:

    def __init__(self):

        self.user_input = None

    def get_user_input(self):

        user_input = input('please choose\n \t rock\n \t paper\n \t scissors').strip()
        if user_input in ['rock']:
            self.user_input = 'rock'
        elif user_input in ['paper']:
            self.user_input = 'paper'
        elif user_input in ['scissors']:
            self.user_input = 'scissors'
        else:
            print('You didn’t choose a option, please try again.')

    def play(self):
       
        self.get_user_input()
    
   