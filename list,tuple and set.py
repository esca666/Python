#LISTS
'''
dummy_list =[]

enter_value = input('Enter value: ')

dummy_list.append(enter_value)

print(dummy_list)
'''
#TUPLE
'''
dummy_list =()

enter_value = input('Enter value: ')

dummy_list.append(enter_value)

print(dummy_list)

#output :- 'tuple' object has no attribute 'append'
'''


#List slicing
 #           [0,         1,     2,  3, 4,5  6   7]

dummy_list = ['ram ' , 'hari' , 5 , 6 ,7,8, 9 , 3]#[start:stop:step] 
               #[start:stop:step] 
print(dummy_list[1:7])
print(dummy_list[1:      7:   2])

print(dummy_list[1:2])

print(dummy_list[:-2])#doesnt inclue the index thats why output is :- ['ram ', 'hari', 5, 6]

print(dummy_list[-2:])#include index thats why output is :- [7, 8]

#SET
a = {1,2,2,6,}
# b = {4,5,6,7,9,}
# now = a-b
# print(now)
