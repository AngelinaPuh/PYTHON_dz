import random 
len = int(input('Количество символов '))
password = "" 
list = ['1',' 2', '3', '4', '5', '6', '7', '8', '9', '0']
for i in range(len): 
    password = password + random.choice(list) 
print(password) 