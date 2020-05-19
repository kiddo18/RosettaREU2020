'''
Problem 1. Age Predictor.

Write a program to predict the "age" of the user. Ask them two questions.

Q1: If I say "up up down down left right left right" what do you say?
(The correct answer to this question is "b a" or "B A").

If they get this question wrong, they are very old. Tell them.
If they get this question right, then you don't really know how old they are. You need to ask them another question.

Q2: What are records made of?
(The correct answer to this question is "vinyl").

If they get this question right, they are old. Tell them. If they get this question wrong, they are young. Tell them.

'''


s = str(input('If I say "up up down down left right left right" what do you say? '))

if not ((s == 'b a') or (s == 'B A')):
    print('You are very old')
else:
    print("Don't know how old you really are")
    q = str(input('What are records made of? '))
    if q != 'vinyl':
        print('You are young')
    else:
        print('You are old')