'''
Problem 3. Repeater

Write a program to take two lists of integers that the user gives you. Prompt for the first list, wait for them to hit enter, then prompt for the second list. The lists must be the same length.

Print out the elements of the first list repeated as many times as requested in the second list.

E.g.

Please enter your first list: 
1 2 3 4 5 6 7
Please enter your second list:
0 2 1 0 3 2 1
Here are your results:
2 2 3 5 5 5 6 6 7

(The first element, 1, is repeated 0 times; the second element, 2, is repeated 2 times; the third element 3 is repeated 1 time; etc.)

If the user gives you two lists of different length, print an error message to the screen instead of printing any numbers.
'''
# User input
s1 = str(input('1st List of integer: '))
s2 = str(input('2nd List of integer: '))

if len(s1) != len(s2): # Catch error
    print('Error! 2 different lengths')
else:
    # Helper function
    def printer(s,n):
        for i in range(n):
            print(s, end=' ')

    # init lists
    li1 = list()
    li2 = list()

    # Populate lists with user inputs
    for char in s1:
        if char != ' ':
            li1.append(int(char))

    for char in s2:
        if char != ' ':
            li2.append(int(char))

    # Print
    for i in range(len(li2)):
        printer(li1[i], li2[i])
        print()

