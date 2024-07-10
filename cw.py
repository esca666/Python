import time
print('welcom to xyz cafe and bar')
time.sleep(1)
user = input('Enter your name : ').lower()
print("Welcome once again to our xyz cafe" ,user)
time.sleep(1)
print('How can i help you Today MR.', user)
print('What you need we have cold drinks only')
cold_drinks = {
    'pepsi':67,
    'fanta':90,
}
print(cold_drinks)
order = input('what you need: ').lower()

if order and cold_drinks:
    print('sorry , we dont have ')
else:
    print('we have')
    

for i in cold_drinks:
    print(i)

