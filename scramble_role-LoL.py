import time
from random import shuffle
import sys

def scramble():
    x = input("Let's Go RANDOM? つ ◕_◕ つ[y/n]\n")
    x = x.upper()
    L=["TOP = ", "JNG = ", "MID = ", "ADC = ", "SUP = "]
    M=["1", "2", "3", "4", "5"]
    if x =="Y":
        print("May TEEMO be With You\n")
        time.sleep(1.5) 
        shuffle(M)
        zip_lm = zip(L,M)
        lst_lm = []
        for L,M in zip_lm:
            print(L+M)    
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            lst_lm.append(L+M)  

        for i in range(len(lst_lm)):
            print(str(lst_lm[i]))
        time.sleep(1)
        scramble()
    if x =="N":
        for i in range(3,0,-1):
            time.sleep(0.5)
            print("Exiting in.."+str(i))
            time.sleep(1)
        exit()
        sys.exit()
    elif x != "Y":
        time.sleep(0.6)
        print('Your Answer Is Incorrect')
        time.sleep(1)
        scramble()
scramble()
