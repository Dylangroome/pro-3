import time
from tictac import main_tic
from rock import main



def intro():
    
    print("Welcome to "  + "!") 

    time.sleep(2)

    while True:
        user = input("Please enter a username: \n")
        if len(user.strip()) == 0:
            print("Invalid username")
            continue
        else:
            break

    time.sleep(2)

    print(f"Hello {user}!")

    while True:
        select = input("Please select a game to continue. Type in 'rock', or 'tic' to play: \n").strip().lower()  # noqa
        time.sleep(2)
        if select == 'tic':
            main_tic()
            break
        elif select == 'rock':
            main()
            break
        else:
            print("You need to enter a valid difficulty to continue...\n")
            continue
        

    time.sleep(2)



intro()