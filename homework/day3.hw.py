# loop, which stops when i enter = 0
# take a number as an input, which is positive, number > 0
# if number > 0, factorial (number)

from math import *

while True:
    number = int(input('Please enter the number --> '))
    if number > 0:
        print(factorial(number))
    if number == 0:
        break
    if number < 0:
        print('Please enter the positive number')
    


#create an empty list
#open loop and ask number 
#if number = 0 stop
#add number to the list
#print every item of the list in reverse order

numbers = []

while True:
    digit = int(input(('Please enter the number --> ')))
    numbers.append(digit)
    if digit == 0:
        numbers.reverse()
        break
   
print(numbers)
    
  