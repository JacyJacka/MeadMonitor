from math import exp
from numpy import random

OFFSET = 1000
NUM_PONTS = 10000

noise = random.normal(0,0.2,NUM_PONTS)
prova_signal = []
for i in range(0,NUM_PONTS):
    if(i<OFFSET):
        prova_signal.append([float(i),0. + noise[i],293.15 + noise[i]])
    else:
        grav = 10*(1-exp((OFFSET-i)/1000)) + noise[i]
        prova_signal.append([float(i),grav,293.15 + noise[i]])

with open("SignalExample.txt", "w") as f:
    for elem in prova_signal:
        f.write(f"{elem[0]}\t{elem[1]}\t{elem[2]}\n")
f.close()