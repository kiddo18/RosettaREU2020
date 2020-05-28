'''
The nth fibonacci number can be computed more efficiently by not using recursion, 
but instead by building up the answer from the bottom.

Create an iterative version of the fibonacci function, fib_iterative, that takes one argument, n, 
and returns the nth fibonacci number.

Allocate a list of length n. Initialize fib[0] = 1 and fib[1] = 1. 
Then fill in each entry in your list in ascending order with:

mylist[i] = mylist[i-1] + mylist[i-2]

Now measure the running time of fib_iterative for each of the fibonacci numbers between 1 and 40. 
How does it computer to the recursive version?

Submit both your function and a plot of its running time.
'''
def fib_iterative(n):
    fiblist = [1,1]
    for i in range(2, n):
        fiblist.append(fiblist[i - 1] + fiblist[i - 2])
    return fiblist

print(fib_iterative(7))
    