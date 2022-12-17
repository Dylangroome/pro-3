# The Carnival

<img width="755" alt="Screenshot 2022-12-17 at 07 08 22" src="https://user-images.githubusercontent.com/108524172/208230376-1dbabcdc-fc20-44a3-be45-fd1785359230.png">

- 🪨 📄  ✂️ 

<img width="790" alt="Screenshot 2022-12-17 at 07 10 08" src="https://user-images.githubusercontent.com/108524172/208230406-f111d9c9-5076-41c7-af34-f799cf64b577.png">

- TicTacToe
- 
<img width="778" alt="Screenshot 2022-12-17 at 07 08 50" src="https://user-images.githubusercontent.com/108524172/208230418-0a8075c9-6383-444f-afd9-ffdc51f2a23f.png">

- Deployed link https://carnival.herokuapp.com/

## Author
Dylan Groome

## Project Overview
![Python Terminal by Code Institute - 17 December 2022](https://user-images.githubusercontent.com/108524172/208230978-3f3190e4-093a-477d-b89c-82330752afbb.gif)

- The carnival is a Terminal which will allow a choice of the games available to play.
- Right now there are two games available 🪨 📄 ✂️ and tictactoe
- I hope to add ore variety in mini game in the future.

## Table of Contents
Generate after readme is complete for UX and below

## How To Play/Use
Greetings and user name input at first site

a brief decrepit on the choices available. 

Input the game you wish to play and you will be brought to a screen where you can start playing. 

Afterwards 
you can choose to play again or end.

## Features
- color code for ease of readability
- Ask for a username input which will be saved
- capital and lower case dont cause a error on input
- text with description about the terminal 
- a choice of game will appear and ask for user input
- wrong input asks to try again
- rock will play 🪨 📄 ✂️ and determine win,loss or tie
- options to play again
- tic will play tic-tac-toe and determine a 3 row sequence win or tie.
- options to play again
- option to end game



### Implemented Features
- score tracker

- tictactoe board

<img width="778" alt="Screenshot 2022-12-17 at 07 08 50" src="https://user-images.githubusercontent.com/108524172/208231512-d614669e-51fe-4685-95ac-5afd67ee2dbb.png">



### Future Features

- more game options
- winning multiple games will achieve tokens to spin for a prize 
- prizes save to user as a collectible to try and get the user to try different games


## Design Documents

<img width="814" alt="Screenshot 2022-12-17 at 07 04 49" src="https://user-images.githubusercontent.com/108524172/208231802-8d18620c-ece7-49c1-90a1-ba844d2aeaf0.png">


## Data Model/ Classes


![image](https://user-images.githubusercontent.com/23039742/130148204-b56406bf-0fff-48f3-9dee-2f3cdbe67cc5.png)

### Class 

### Player
A player is a generic representation of a player.


### RandomComputerPlayer
A RandomComputerPlayer is the computer, it is an extension of the BasePlayer class.
 

### HumanPlayer
A HumanPlayer represents the human player. It is an extension of the BasePlayer class.
 
### TicTacToe
Stores the board,inputs and outcomes for the game tictactoe

### Game
Stores the options,inputs and outcomes for the game 🪨 📄 ✂️ 


**Properties**

A representation of the game of TicTacToe.

Properties
- self.board an array of 9 entries representing positions.
- self.current_winner keep track of winner
- o_player representing the computer.
- x_player representing the human user.

A representation of the game 🪨 📄 ✂️ 

Properties
- self.comp_wins = comp_wins = set computer wins
- self.player_wins = player_wins = set player wins
- self.games_played = games_played = set games played
- self.user_input = None = set user choice to none
- self.computer_choose = None = set computer choice to no

**Methods**

A representation of the game of TicTacToe.

Method
- def print_board = tictactoe grid in terminal
- def print_board_nums = which number corresponds with each box
- def available_moves = checks available moves
- def make_move = if valid move make move
- def winner = checks winner
- def play = Calls functions, iterate while empty square and alter letter after move.
- def main_tic = gives user option play the game.

A representation of the game 🪨 📄 ✂️ 

Method
-  def get_user_input = user input
-  def get_computer_input = Generates the computer's choice.
-  def display_match_results = Display's and adds player wins and computer wins.
-  def winner = adds score and shows appropriate message for wins/ losses/ ties.
-  def play_again = Gives user option to play another round.
-  def play = Calls functions to get user and computer choice, get the match results and the play again function.
-  def main = gives user option play the game.

## Libraries used

- Time: used the sleep() function in between messages to the user to allow time for reading.
- Random: used to randomize the computer's moves.
- Colorama: used to color code the text.


## Testing


### Validation Testing

I used pep8 (https://pep8ci.herokuapp.com/#) to validate my python code.

run.py file

github validation.

<img width="1398" alt="Screenshot 2022-12-17 at 04 28 22" src="https://user-images.githubusercontent.com/108524172/208224866-bfede2d0-0e7a-4bae-983e-06ca77f781b8.png">

pep8 validation.

<img width="1440" alt="Screenshot 2022-12-17 at 04 34 52" src="https://user-images.githubusercontent.com/108524172/208225328-e936a8f4-0704-43f4-8a17-9cd97dc6ad4f.png">

tictac.py file

github validation.

<img width="1404" alt="Screenshot 2022-12-17 at 04 40 17" src="https://user-images.githubusercontent.com/108524172/208225462-bead63db-9bab-480f-a5b9-f999a81553f6.png">

pep8 validation.

<img width="1421" alt="Screenshot 2022-12-17 at 04 41 07" src="https://user-images.githubusercontent.com/108524172/208225476-e6731340-bcca-43d5-985c-aa2db562e5e5.png">


rock.py file

github validation.


<img width="1431" alt="Screenshot 2022-12-17 at 04 45 51" src="https://user-images.githubusercontent.com/108524172/208225595-aeb705f4-3b64-4404-9ee4-f6c666783069.png">

pep8 validation.


<img width="1422" alt="Screenshot 2022-12-17 at 04 44 02" src="https://user-images.githubusercontent.com/108524172/208225608-0e14f2d7-2b6a-445e-88a6-83f21cec0694.png">



If the line is too long just add 
```$python 
# noqa
```
There is a space before the # and after it to skip the quality assurance for that line.

### Manual Testing

Username 
1. Arrive on app page on Heroku.
2. Try to input a blank username.
3. Get error message.
4. Try to input a valid username.

Making a move
1. Try to type in anything other than the optional input.
2. Get an error message.
3. Try to type a valid option.
4. Verify the right game is displayed.
5. Verify that the number has been taken away from the ""Available Moves"" board.
6. Verify that the numbers that were input previously cannot be input again."
7. Verify the computer displays a option

Ended 
1. Select ""N"" to exit.
2. Check that the game exits the play loop.
3. Check that the game says goodbye.


- [ ] invalid entry, says try again  and repropts
- [ ] no entry, says try again and reprompts


### Defect Tracking

- games would run before asking username and greeting when main function was imported 

fix was to remove main function 
call from rock.py and tic.py

- Error when uppercase input 

fix was to add the .lower to inputs request

- not breaking 
 from a while 
 caused the game to continue 
 Infinity 

fix was to add a break to while loop


## Deployment



### Gitpod
- Click Gitpod button or add it if you don't have it to chrome. 
  - Once Gitpod is open, type ```pip3 install -r requirements.txt``` in the terminal. 
  
  - Then type ```python3 run.py``` in the terminal. This will start the game. 
  




### Heroku

- 1) Head to [Heroku](https://heroku.com) and create an account.
- 2) Click on "Create New App".
- 3) Name your app, select your region and click on "Create app"

- 4) On your app's dashboard bar, click on "Settings" and then click on "Reveal Config Vars".

- 5) 
<img width="996" alt="Screenshot 2022-12-17 at 09 47 27" src="https://user-images.githubusercontent.com/108524172/208236049-e4856833-3db1-4b29-b596-51f3db34f382.png">



- 6) Scroll down and click on "Add buildpack", select "python" and "Save changes".
- 7) Repeat step 6 and select "nodejs" instead of "python" (they should be added in that order, python first and nodejs after).

<img width="830" alt="deployment4" src="https://user-images.githubusercontent.com/82375381/132575097-06258f70-6951-44da-9573-3c9523c839c6.png">

- 8) On your app's dashboard bar, click on "Deploy" and on the "Deployment method" section, select "GitHub".

<img width="984" alt="deployment6" src="https://user-images.githubusercontent.com/82375381/132575228-308886b3-996d-4375-93b1-201bfc030dac.png">

- 9) Search for your GitHub repository and click "Connect".


- 10) Scroll down and click on "Enable Automatic Deploys".

<img width="1223" alt="deployment8" src="https://user-images.githubusercontent.com/82375381/132575399-29ded428-305b-4ef8-a7b1-4bd09ebdd1fc.png">

- 11) Wait until all files have been installed and it should give you a "Your app was successfully deployed." message.

<img width="835" alt="deployment9" src="https://user-images.githubusercontent.com/82375381/132575430-ceb70299-cb54-4f99-8a6c-301149a1332c.png">

## Credits

### Code Institute

- [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.


### Tutorials

- https://www.youtube.com/watch?v=8ext9G7xspg&t=4342s

### GitHub
https://github.com/KateEllen/Rock-Paper-Scissors/blob/main/README.md
https://github.com/gabriel-alves-p/noughts-n-crosses/edit/main/README.md


### Acknowledgments

This project could only come to exist because of the help and support from:

- My Code Institute mentor Malia Havlicek for being incredibly helpful and accessible.
- Code Institute for providing the accessible content from which I learned these new skills from.


