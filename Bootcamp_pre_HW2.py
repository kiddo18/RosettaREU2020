def print_star():
    print('*', end='')
    

def print_space():
    print(' ', end='')



def print_tree(h):
    # Print top of tree
    for row in range(1, h+1):

        n_of_space = h - row
        # Print space on each row
        for j in range(n_of_space):
            print_space()

        # Print star on each row
        for i in range(row):
            print_star()
        
        for i in range(row-1):
            print_star()

        # Print space on each row
        for j in range(n_of_space):
            print_space()

        print()
    
    # Print base of tree
    for i in range(h-1):
        print_space()
    print('|')


    
h = int(input('Tree height: '))
print_tree(h)