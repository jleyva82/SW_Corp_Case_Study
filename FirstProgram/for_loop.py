numbers = [1,2,3,4,5,"element", [1,2,3], {"a",4,5.6}]       #our sample list

for item in numbers:                                        #'item is what each element in list is called within list 'numbers'
    print(item)                                             #command will execute for all items in list

l = len(numbers)                                            #calculate the length of the list
print('The length of the list is',l)
