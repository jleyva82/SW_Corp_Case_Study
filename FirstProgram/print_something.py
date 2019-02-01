                                                    #common practice to leave two lines of empty space when defining a fucntion

def print_something(Name="SOMEONE",Age ='UNKNOWN'): #Name and Age are arguements whose value can be changed upon fucntion call out
    print("My name is", Name, "and my age is", Age) #this is what the fuction does. could comma separated values as appose to concatenation

print_something() #executes function with base arguements
print_something(Name= 'Jesus Leyva') #changes value of Name to "Jesus Leyva"
print_something("Anthony Villalobos", 14) #changes value of Name to "Anthony Villalobos" and Age to 14
print_something("Maria Leyva", Age=41) #changes value of Name to "Maria Leyva" and Age to 41
