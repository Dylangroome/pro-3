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

### Requirements
If the user is required to have certain keys and credentials you should include this section with diretions on how to get the necessary information.
ex)
1. **Google Account:** In order to have this program work, you need a google account. If you don't have one  [Create a google account](https://accounts.google.com/Signup)
2. **Google APIs**
    1. in a new incognito tab, log into your new google account.
    1. then update the url to be: https://console.cloud.google.com/getting-started?pli=1 
        
        **GOOGLE DRIVE API Access**
        1.  create a new project for this, call it XXXXXX (You might want to refer to what you see in this video: https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/ at the bottom of the screen to write out steps.)
        2. Then click on Add APIs and Services and select Libraries
        3. Search for Google Drive
        4. Click Enable
        5. Click Create Credentials
        6. Select Google Drive API from the drop down, Application Data, then no and click the Next Button
        7.  (https://developers.google.com/drive/api/v3/enable-drive-api) 
        8. for service account details fill in a service account name ex) xxx_API, then click Create and Continue
        9. For the Accoun acces, select Role: Basic/Editor then continue
        10. Then Click Done
        11. Now select the newly created service account
        12. Click on the KEYS Tab
        13. Click Add Key
        14. Select JSON type (right click to show in folder so you know where the file was saved.
        
        **GOOGLE SHEETS API Access**
        You may need to us the back button get to the APIS & SErvices section from where you were.
        1. click the Libray  Tab and serarch for Google Sheets
        2. click enable

3. The downloaded credentialsJSON file is basically your creds.json file that you need to put into your heroku settings or gitpod environment to access your google drive.

4. Google Sheet Template
  - If you had to create specific sheets for your project, instruct users to make their own copy of it from yours and rename it back to what the python project expects
  - And don't forget to share the spreadsheet in question with the client_email from the creds.json 
### Gitpod
This section should describe the process someone would have to go through to get the local working in gitpod.  Such as install requirements.txt  and setting up a creds.json file that is in the gitignore and keeping their workspace.

If you have project settings required such as a creds.json file from the GOOGLE DRIVE API acess, please provide an example of that file in the writeup with the project key values:
```$python
{
    "type": "service_account",
    "project_id": "<YOUR_VALUE>",
    "private_key_id": "<YOUR_VALUE>",
    "private_key": "<YOUR_VALUE>",
    "client_email": "<YOUR_VALUE>",
    "client_id": "<YOUR_VALUE>",
    "auth_uri": "https://accoutns.google.com/0/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cer_url": "https://www.googleapis.com/oauth2/v1/certs",
    "clien_x509_cert_url": "<YOUR_VALUE>"
}
```

If you have any dependencies, you should instruct users to install them
```$python
pip3 install -r requirements.txt
```



### Heroku
This section should describe the process you went through to deploy the project to Heroku. Include screenshots if you think they would make the process easier.

You may want to re-watch the [python essentials deployment video](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/e3b664e16366444c8d722c5d8340b340/?child=first) when writing up this section.


If you have project settings required for Heroku, provide a table of the keys and values.
Do not share your personal keys but either cut them out of the screen shot or say <YOUR_VALUE> and include links on how the user would obtain such values.

#### Fork the repository
Make a fork so you have a copy of the repository in your own git hub account: https://github.com/maliahavlicek/portfolio_project_03

![image](https://user-images.githubusercontent.com/23039742/132136504-eb79a6f3-0205-4c82-80c2-eef136ec7e4c.png)


#### New Project
Log into Heroku and create a new project. Name it something like XXX_coders_bistro.


#### Settings
On the settings tab you have to address two things:
1. **Config Vars**

  ![image](https://user-images.githubusercontent.com/23039742/132135869-215d2e0f-805d-40a8-a8c2-fb1098e2645d.png)

  At a bar minimum you should show the user that they need to add the PORT. 8000 key value pair.


2. **Build Packs**

  ![image](https://user-images.githubusercontent.com/23039742/132135918-28cac112-7766-4277-905c-4a4963d8442d.png)

  add Python Then Node.js


#### Deploy
1. Set up to github and select the correct repository:

  ![image](https://user-images.githubusercontent.com/23039742/132136113-c257c921-d10c-4ccc-af09-6a1d25136395.png)

2. Deploy either manual or automatic

![image](https://user-images.githubusercontent.com/23039742/132136241-9d76fabb-39f0-4696-bc5f-047398fdaf41.png) 



## Credits

To avoid plagiarism amd copyright infringement, you should mention any other projects, stackoverflow, videos, blogs, etc that you used to gather imagery or ideas for your code even if you used it as a starting point and modified things. Giving credit to other people's efforts and ideas that saved you time acknowledges the hard work others did. 

-[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

### Content

Use bullet points to list out sites you copied text from and cross-reference where those show up on your site

### Media

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site. This includes attribution for icons if they came from font awesome or other sites, give them credit.

### Acknowledgments

This is the section where you refer to code examples, mentors, blogs, stack overflow answers and videos that helped you accomplish your end project. Even if it's an idea that you updated you should note the site and why it was important to your completed project.

If you used a CodeInstitute Instructional project as a starting point. Make note of that here too.


