import random
import time
import datetime as datetime
import webbrowser as brw


def choose():
    options = ["Flip a Coin", "Search"]
    availArgs=[]
    for i, option in enumerate(options):
        print(f'{i + 1}: {option} ')
        availArgs.append(i+1)
    choice=input("Choose an option >>  ")
    if int(choice) not in availArgs:
        print(f'No such option "{choice}".')
    else:
        return int(choice)
        

def tossCoin():
    choice = ["Heads", "Tails"]
    return choice[random.randint(0,1)]

def multiToss(arg1):
    count = 0
    outcome = []
    while count < arg1:
        toss = tossCoin()
        print("Flipping...")
        time.sleep(1)
        print(toss)
        count += 1
        outcome.append(toss)
    print(f"----------------")
    print(f'Heads has occured: {outcome.count("Heads")}\n\nTails has occured: {outcome.count("Tails")}\n')

def google():
    i=input("Enter your query >>  ")

    if i.startswith(("!g", "!google")):
        iG = i.replace('!google', '', 1).replace('!g', '', 1)
        brw.open_new_tab(f'https://www.google.com/search?hl=en&q={iG}')

    elif i.startswith(("!ya", "!y", "!yandex")):
        iY = i.replace("!yandex", '', 1).replace("!ya", '', 1).replace("!y", '', 1)
        brw.open_new_tab(f"https://yandex.com/search/?text={iY}")

    else:
        iD = i.replace('?', '%3F&')
        brw.open_new_tab(f"https://duckduckgo.com/?q={iD}")
        
if __name__ == "__main__":

    def tossit():  
        i = int(input("How times toss a coin? >>  "))
        if i == 1:
            print("Flipping...")
            time.sleep(1)
            print(tossCoin())
        elif i < 1:
            print(f'Exitting because the given value was "{i}"...')
            exit
        else:
            multiToss(i)
            
            
    choice = choose()
    if choice == 1:
        tossit()
    elif choice == 2:
        google()
    else:
        exit
