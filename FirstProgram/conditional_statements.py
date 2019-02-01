
check = 'hamburger'                                 #variable designation

if check == False:                                  #begin conditional statement if the variable is boolean False
    print("it is false")                                #then print "it is False'
elif check == 'hamburger':                          #if the varianble is not boolen False but string 'hamburger'
    print("yum, hamburgers")                            #then print "yum, hamburgers"
elif check == 'yo':                                 #if the variable is neither False or "hamburger' but it is 'yo'
    print('Hello')                                      #then print 'Hello'
else:                                               #catch all, if none of the statements above are True
    print('it is actually equal to True')               #then prin "it is actually equal to True