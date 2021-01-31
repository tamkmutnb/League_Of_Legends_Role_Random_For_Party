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
        for L,M in zip(L,M):
            print(L+M)    
            time.sleep(2)
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
