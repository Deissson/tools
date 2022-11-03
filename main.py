import random
import time

def choose():
    options = ["Flip a Coin", "Time Calculator"]
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
    
def calculateTime():
    inputTime = input("Type time you want to [Press Enter to use your current time ] >>  ")
    if len(inputTime) < 1:
        current_time = time.strftime("%H:%M", time.localtime())
        addTimeM = input(f"How much minutes to add for {current_time} >>  ")
        addTimeH = input(f"How much hours to add for {current_time} >>  ")
        if len(addTimeM or addTimeH) < 1:
            print('Skipping...') 
    else:
        addTimeM = input(f"How much minutes to add for {inputTime} >>  ")
        addTimeH = input(f"How much hours to add for {inputTime} >>  ")

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
        calculateTime()
    else:
        #print(f'No such option "{choice}".')
        exit
