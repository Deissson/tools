import random
import time

def main():
    choice = choose()
    if choice == 1:
        print(tossCoin())
        time.sleep(3)
        main()
    elif choice == 2:
        tosses = 0

        try:
            tosses = int(input("How many times do you want to toss a coin?: "))
            multiToss(tosses)
            time.sleep(3)
            main()
        except Exception:
            print("Invalid choice!")
            time.sleep(3)
            main()

    elif choice == 3:
        try:
            limit1 = int(input("What should the minimum number be?: "))
            limit2 = int(input("What should the maximum number be?: "))
            print(random.randint(limit1, limit2))
            time.sleep(3)
            main()
        except Exception:
            print("Invalid choice!")
            time.sleep(3)
            main()

    else:
        print(f'No such option "{choice}".')
        time.sleep(3)
        main()


def choose():
    print("""Options: 
    [1]: coinflip
    [2]: multiple coinflips
    [3]: random number
    """)

    try:
        choice=input("Choose an option >>  ")
        return int(choice)
    except Exception:
        return str(choice)
        

def tossCoin():
    choices = ["Heads", "Tails"]
    return random.choice(choices)

def multiToss(arg1):
    count = 0
    outcomes = []
    while count < arg1:
        toss = tossCoin()
        time.sleep(1)
        print(toss)
        count += 1
        outcomes.append(toss)
    print(f'Heads has occured: {outcomes.count("Heads")} times\nTails has occured: {outcomes.count("Tails")} times\n')
    
if __name__ == "__main__":

    #def tossit():  
    #    i = int(input("How times toss a coin? >>  "))
    #    if i == 1:
    #        time.sleep(1)
    #        print("Flipping...")
    #        print(tossCoin())
    #    elif i == 0:
    #        print(f'Exitting because the given value was "{i}"...')
    #        exit
    #    else:
    #        multiToss(i)
            
            
    main()
        
