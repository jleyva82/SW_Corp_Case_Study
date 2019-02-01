                                                    #common practice to leave two lines of empty space when defining a fucntion

def print_people(*people):                          #arguement is array call 'people'
    for person in people:                           #creates a for loop that continues for all 'person' oulined in function call out
        print('this person is', person)             #execution of function is to print "this person is' + " " + name of person as indicated in function call out

print_people("Nick", "Dan", 'Jesus', "king")        #function call out includes 4 arguements, thus there will be 4 loops of print function 
