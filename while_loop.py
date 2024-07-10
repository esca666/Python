#while loop

appended_number = []
user_input = input('Enter your name: ')

while user_input.isdigit():#isdigit is the string method
    user_input = input('Enter number: ')
    appended_number.append(user_input)
    
print(appended_number)
