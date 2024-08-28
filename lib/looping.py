#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    # code goes here!
    squared_list= [x**2 for x in int_list]
    return squared_list
print(square_integers([1,2,3]))

def fizzbuzz():
    # code goes here!
    for i in range (1, 101):
        # print(i)
        if i % 3 == 0 and i % 5 == 0: 
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 ==0:
            print('Fizz')
        else:
            print(i)
fizzbuzz()