# my_table = int(input('Enter the number: '))

# for i in range (1,11):
#     i*=my_table
#     print(f"{my_table * i}")
total =0
for i in range (1,10):
    
    number = int(input('enter the num: '))
    
    ques = input('Do you want to processed , skip , break(p/s/b): ')
    total+=number
    if ques=='p': 
        print('you wanna prossed again ')


    elif ques =='s':
     print('skipped')
    else:
       break
    print(total)
