

def do_math(num1, num2):                                #funcition named 'do_math' with two parameters num1 and num2
    return num1 + num2                                  #generates addition of arguemtns given in call out
                                                        #note that it does not print unless it is later called upon by a print function
math1 = do_math(5,7)                                    #run function with given arguemnts and store into 'return' into variable 'math1'
math2 = do_math(11,34)                                  #run it again into 'math2'

print('first sum is', math1, 'second sum is', math2)    #outputs given statement
