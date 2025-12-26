''' this is my third github project '''

import random   

user_name= input("Enter Your Name: ")
print(f"Hi {user_name}\nWelcome to the hangMan Game.")

fruits= ''' apple banana orange mango grapes pineapple strawberry watermelon papaya pear '''
vegetables= '''carrot potato tomato onion spinach cabbage broccoli cauliflower peas eggplant '''

# get the user choice either vegetables or fruits
while True:
    user_choice= input('Enter Your choice\n enter "v"--> vegetables\n enter "f"--> fruits\n --------------------->: ').lower()
    if user_choice.strip()== 'v' or user_choice.strip()== 'f':
        break
    else:
        print('Invalid Input.')
        continue 
