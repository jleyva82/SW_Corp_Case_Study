run = True                           #setting starting parameter, want it to run at least one
current = 1                          #staring at counter of 1

while run:                           #while current is less than 100 loop will run
    if current == 100:
        run = False                  #once the value of current is equal to 100 the value of run will be boolen False
                                     #meaning the while contition is met and loop will stop running
    else:
        print(current)               #function is to print value
        current += 1                 #short hand of succesor is "+="

print("I have stopped counting because I have reached", current)