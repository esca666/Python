 #Alert if critical value is triggered

 value = int(input('enter the value: '))

 while value < 100 and value > 0 :
     value = int(input('enter the value: '))
     # print('drilling')
 print('we stooped')
username1 = "admin"
pasword1 = "abcd"
i = 0
while i < 3:
    
    username = input('Enter the username : ')
    password = input('Enter the password : ')
    if username == username1 and password ==pasword1:
        print('Granted')
        break
    i += 1