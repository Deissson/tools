import random
import time

def choose():
    options = ["Flip a Coin", "Calculator"]
    for i, option in enumerate(options):
        print(f'{i + 1}: {option} ')
    choice=input("Choose an option >>  ")
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
    
if __name__ == "__main__":

    def tossit():  
        i = int(input("How times toss a coin? >>  "))
        if i == 1:
            time.sleep(1)
            print("Flipping...")
            print(tossCoin())
        elif i == 0:
            print(f'Exitting because the given value was "{i}"...')
            exit
        else:
            multiToss(i)
            
            
    choice = choose()
    if choice == 1:
        tossit()
    elif choice == 2:
        print("WIP")
    else:
        print(f'No such option "{choice}".')
        
