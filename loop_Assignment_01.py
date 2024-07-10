#write a python program that prints all the even numbers from 1 to 100.
for num in range (1,100):
    if num %2==0:
        print(num)

#create a list of numbers and write a for loop to calculate and print the sum of all number in the list
my_list=[10,30,40,60]
total = 0

for num in my_list:
    total+=num

print('The sum of my_list: ', total)