#CONDITIONAL STATEMENTS
my_dict = {
    '1':'ram',
    '2':'shyam'
}

my_keys = my_dict.keys()
my_value = my_dict.values()

roll_no =input('Enter the roll no: ')

if roll_no in my_keys :
    print('Key already exists')
else:
   name =input('Enter the name : ')
   if name in my_value:
        print('Already Exists')
   else:
        print("It doesnt exists")
        print("Adding the name... please wait .")
        print('Added successfully.')


   my_dict.update({
    roll_no:name
   })
   
   print('students', my_dict)