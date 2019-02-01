import os            #imports from "os" library
import sys           #imports from "sys" library. note we separated each import into its own line
#from MyModule import foo, bar, foobar                      #imports from "MyModule" the tools "foo", "bar" and "foobar"


def my_function(one, two,             #leave two empty lines between imports and subsequent code
                three, four,
                five, six):           #separate parameters so that they are easy to see
    print('hello world')

                                  #leave 2 spaces between function call outs
def second_function():
    print('second function')


my_list = [1,2,                   #when creating a list, vertically align values when necessary
           3,4,
           5,6]

print( "Hello World" )  #dont do this, no unnecessary white spaces
v = my_list[ 2 ]


check = True

if check is True: print("This is true")    #dont do this. do not continue code after colon indicating if statement

my_function(1,2,3,4,5,6); second_function()        #when calling multiple functions, use "; " to seperate them


#THESE are the PEP Guidelines (accepted sentence structure when coding
#no unnessary white spaces
#vertically align values when posible, such as in list or for parameters
#dont continue to write in same line after ":" has been placed
#import from one Module / Library at a time
#use common sense
#visually asthetic and easy to read

