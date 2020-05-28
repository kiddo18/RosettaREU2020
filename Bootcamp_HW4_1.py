'''
One fun thing about functions is that they can call themselves.

Write a function "fib" that takes one argument, n, and returns the nth fibonacci number. 
The fibonnaci sequence is given by the recusive formulation

fib(i) = fib(i-1) + fib(i-2)
Order:  1 2 3 4 5 6 7
Output: 1 1 2 3 5 8 13
and then by a termination criteria that fib(1) is 1 and fib(2) is also 1.

Write the fib function so that it calls itself. Measure the running time to compute 
each of the fibonacci numbers between 1 and 40 and create a plot with your favorite plotting tool 
(I don't care what you use).

Why is it so slow to compute the 40th fibonacci number?

Submit both your function and your plot
'''
import numpy as np
import matplotlib.pyplot as plt
import time

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(7))

x = np.zeros(40)
y = np.zeros(40)
for i in range(1, 41):
    time_start = time.time()
    x[i] = fib(i)
    time_stop = time.time()
    y[i] = time_stop - time_start

plt.plot(x,y)