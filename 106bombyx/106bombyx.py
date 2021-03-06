#!/usr/bin/python2.7

import matplotlib.pyplot as plt
import os, sys

########################################################################## 

if len (os.environ) == 37:
    print('Environnement changed')
    sys.exit(1)

##########################################################################

if len (os.environ) == 0:
    print('Environnement delete')
    sys.exit(1)

##########################################################################   

if len (sys.argv) < 2 or len (sys.argv) > 3:
    print('You need to put 1 or 2 argument!')
    sys.exit(1)

##########################################################################   

if len (sys.argv) == 2:
    try:
        float(sys.argv[1])
    except:
        print('Your number is not correct')
        sys.exit(1)
    k = float(sys.argv[1])
    if k < 1 or k > 4:
        print('You can only put a number between 1 and 4!')
        sys.exit(1)
    x1 = 10
    list_one = []
    list_two = []
    a = 0
    while a < 101:
        list_one.append(a)
        list_two.append(x1)
        x1 = k * x1 * (1000 - x1)/1000
        a = a + 1
    plt.plot(list_one, list_two, 'b-o')
    plt.title('106bombyx')
    plt.ylabel('nombre de bombyx')
    plt.xlabel("nombre de generation")
    plt.show()  

##########################################################################

if len (sys.argv) == 3:
    try:
        int(sys.argv[1])
    except:
        print('Your number 1 isn\'t correct')
        sys.exit(1)
    try:
        int(sys.argv[2])
    except:
        print('Your number 2 isn\'t correct')
        sys.exit(1)
    av1 = int(sys.argv[1])
    av2 = int(sys.argv[2])
    list_one = []
    list_two = []
    x1 = float(10)
    k = 1
    if av1 >= av2:
        print('your number 2 is superior or equal to the first number!')
        sys.exit(1)
    while k <= 4:
        c = 1
	x1 = float(10)	
        while c <= av1:
            x1 = k * x1 * ((1000 - x1)/1000)
            c = c + 1
        while c <= av2:
            list_one.append(k)
            list_two.append(x1)
            x1 = k * x1 * (1000 - x1)/1000
            c = c + 1
        k = k + 0.01
    plt.plot(list_one, list_two, ',')
    plt.title('106bombyx')
    plt.ylabel('nombre de bombyx')
    plt.xlabel("Taux de croissance")
    plt.show()

