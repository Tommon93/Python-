new_list = [1,2,3]
result = new_list[0]
result

new_list[10] #out of range - gives error

#Search using in operator
if 1 in new_list:
    print(True)

#Using for loop
for n in (new_list):
    if n == 1:
        print(True)

        break

#Arrays - empty lists 
numbers = [] #Creates an empty list of space of size n+1
#The space allocated by the list and the space used by the list is not the same. 
len(numbers) #Does not use memory allocation as an indicator of it's size - because it has space for 1 element
numbers.append(2)
numbers.append(200) #Python is resizing it's allocated memory to accomdate the extra element - called: list resizing 
#Creates four contiguous blocks of memory for the list resizing (see below)
#The growth pattern for lists in python is: 0,4,8,16,25,35,46... 
#So when the elements are approaching these values - the list resizes again

#Extend
numbers = []
numbers.extend([4,5,6])
numbers
#Extend takes another list to add - essentially takes a series of appends calls to each of the elements in the new list untili all of them are
#appended to the original list. 
#This operation has a run time of O(k)


