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