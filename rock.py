import random


class Game:

    def __init__(self):

        self.user_input = None
        self.commuter_choose = None

    def get_user_input(self): # user input 

        user_input = input('please choose\n  rock\n  paper\n  scissors\n').strip()
        if user_input in ['rock']:
            self.user_input = 'rock'
        elif user_input in ['paper']:
            self.user_input = 'paper'
        elif user_input in ['scissors']:
            self.user_input = 'scissors'
        else:
            print('You didn’t choose a option, please try again.')




    def get_commuter_input(self):
        


    def play(self):
       
        self.get_user_input()

        


def main():
    
    

    game = Game()
    
    
    while True:

        
        
        return game.play()
        


main()
