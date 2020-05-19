'''
Problem 2. Sorter.

Write a program to sort a list of integers that the user gives you. Prompt the user to give you a list of integers, separated by spaces, and then hit enter. Once they've hit enter, 
1. convert the string that you are given into integers, and
2. put those integers into a python "list".

(A list in python is an array; it has the insertion and access complexity of an array and not a typical computer-science-class "list." They're called lists anyways.)

After you have created the list, use a function that list provides (google for it!) that will sort the contents of the list in ascending order.

Then print the sorted list to the screen for the user.

You may assume that the user is not going to input "five" to mean the number 5 or give you any non-integer inputs.

'''
s = str(input('List of integer: '))

li = list()
for char in s:
    if char != ' ':
        li.append(int(char))

li.sort()
print(li)