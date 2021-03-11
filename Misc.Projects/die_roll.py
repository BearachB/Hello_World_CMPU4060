import random
import time
def die_roll():
        die_sides = int(input("How many sides do you want on your die?: "))
        die_number = random.randint(1,die_sides)
        stop_val = 0
        pos_ans = ['y','Y','Yes','yes','YES','yES','yeS',]
        neg_ans = ['n','N','No','no','NO']
        print("You rolled a", die_number)
        chance = 1/die_sides
        print("Probability = ", chance)
        time.sleep(1)
        while(stop_val==0):
            mark = str(input("Do you want to re-roll the die? Y/N: "))
            if (mark in pos_ans):
                die_sides = int(input("How many sides do you want on your die?: "))
                die_number = random.randint(1,die_sides)
                time.sleep(0.4)
                print("You rolled a", die_number)
                chance = 1/die_sides
                print("Probability = ", chance)
                time.sleep(1)
            elif (mark == 'n' or mark == 'N' or mark == 'no' or mark == 'No' or mark == 'NO'):
                print ("You have chosen to end the game")
                stop_val = 1
                break
die_roll()
