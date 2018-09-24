# CMPT 120L 113
# Fibonacci Calculator
# Author: Ian Miller
# Created: 24 Sep 2018

fibOne = 0
fibTwo = 0
answer = 1


def fibCalc ():
    global fibOne
    global fibTwo
    global answer
    fibTwo = fibOne
    fibOne = answer
    answer = fibOne+fibTwo

n = int(input("Enter a number: "))

for i in range(n-1):
    fibCalc()
print(answer)
    
   
    



