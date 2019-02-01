import re                                         #import external library for regex to safe keep the evalfunction by removing extra characters

print('Magical Calculator')                   #title for UI
print('Type "quit" to exit')                    #legent to quit for UI
print('Type "clear" to reset\n')

previous = 0                                      #starting ans is 0
run = True                                        #starting conditon for our while loop

def performMath():                                #creating our math function
    global run                                    #must dictate our variable as global so the it can be altered for our while loop
    global previous
    equation = ""

    if previous == 0:
        equation = input('Enter Equation:')       #ask for input equation to start with
    else:
        equation = input(str(previous))           #if previous value still in place, report it while waiting for new input


    if equation == 'quit':                        #have an exit strategy
        print("Goodbye. Thank you for using Magical Calculator.")                    #notify user of exit
        run = False                               #change global value to impact while loop

    elif equation == 'clear':                     #insert clear UI
        previous = 0                              #reset previous value to 0

    else:                                                       #unless user has input 'quit'
        equation = re.sub('[a-zA-Z,():;" "]', '', equation)     #must elimate dangerous characters for eval function, this is why we imported regex

        if previous == 0:
            previous = eval(equation)                     #take altered input, only numbers and operations, and perform evaluation
        else:
            previous = eval(str(previous) + equation)       #if other value already in previous take it and add new equation to it



while run:                                         #run function of 'performMath' as long as run == True
    performMath()


#note that this is an elegant version of a calculator using the eval command + regex library
#instead of a each defining a function for each operation and having the UI allow for selection of function
#in conjuction of conditional if statement for each function 