import random
import time
import datetime as datetime
import webbrowser as brw

class tools:
    def choose(): # Generates a list with options and return a user's choice
        
        #List of options for a list
        options = ["Flip a Coin", "Search"]
        # Generating a list with options
        for i, option in enumerate(options):
            print(f'{i + 1}: {option} ')
        while True:
            try:
                choice=input("Choose an option >>  ")
                return int(choice)
            except Exception:
                print("\nOnly regular numbers are allowed!\n")
            

    def tossCoin(arg1=None): # Returns Heads/Tails
        #Available options
        choice = ["Heads", "Tails"]
        if arg1 == "tossOnce":
            try:
                i = int(input("How many times toss a coin? >>  "))
                if i == 1:
                    print("Flipping...")
                    time.sleep(1)
                    print(tools.tossCoin())
                elif i < 1:
                    print(f'Exitting because the given value was "{i}"...')
                    exit
                else:
                    tools.multiToss(i)
            except Exception:
                print("\nOnly regular numbers are allowed!\n")
        else:
            return choice[random.randint(0,1)]
        

    def multiToss(arg1): # Tosses a coin multiple times, heavily based on tossCoin
        count = 0
        outcome = []
        
        while count < arg1:
            toss = tools.tossCoin()
            print("Flipping...")
            time.sleep(1)
            print(toss)
            count += 1
            outcome.append(toss)
        
        print(f"----------------")
        print(f'Heads has occured: {outcome.count("Heads")}\n\nTails has occured: {outcome.count("Tails")}\n')

    def search(): # Searches the web using 3 search engines
        i=input("Enter your query >>  ")

        # Search using Google
        if i.startswith(("!g", "!google")):
            iG = i.replace('!google', '', 1).replace('!g', '', 1)
            brw.open_new_tab(f'https://www.google.com/search?hl=en&q={iG}')
            
        # Search using Yandex
        elif i.startswith(("!ya", "!y", "!yandex")):
            iY = i.replace("!yandex", '', 1).replace("!ya", '', 1).replace("!y", '', 1)
            brw.open_new_tab(f"https://yandex.com/search/?text={iY}")
            
        # Search using DuckDuckGo (Default)
        else:
            iD = i.replace('?', '%3F&')
            brw.open_new_tab(f"https://duckduckgo.com/?q={iD}")
            
    def __init__(self) -> None: 
        print('''

████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
   ██║   ██║   ██║██║   ██║██║     ███████╗
   ██║   ██║   ██║██║   ██║██║     ╚════██║
   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                           

''')
        choice = tools.choose()
        if choice == 1:
            tools.tossCoin("tossOnce")
        elif choice == 2:
            tools.search()
        else:
            print(f'No such option "{choice}".')
            exit
            
if __name__ == "__main__":
    tools()
