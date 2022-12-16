import time
from colorama import Fore, Back, Style
from tictac import main_tic
from rock import main


def intro():

    print(Fore.BLUE + "Welcome to The Carnival " + "!")

    time.sleep(2)

    while True:
        user = input(Fore.GREEN + "Please enter a username: \n")
        if len(user.strip()) == 0:
            print(Fore.RED + "Invalid username")
            continue
        else:
            break

    time.sleep(2)

    print(f"Hello {user}!")

    while True:
        select = input(Fore.GREEN + "Please select a game to continue. Type in 'rock', or 'tic' to play: \n").strip().lower()  # noqa
        time.sleep(2)
        if select == 'tic':
            main_tic()
            break
        elif select == 'rock':
            main()
            break
        else:
            print(Fore.RED + "You need to enter a valid option to continue...\n")
            continue

    time.sleep(2)


intro()
