''' this is my third github project '''

import random   

user_name= input("Enter Your Name: ")
print(f"Hi {user_name}\nWelcome to the hangMan Game.")

fruits= "apple banana orange mango grapes pineapple strawberry watermelon papaya pear"
vegetables= "carrot potato tomato onion spinach cabbage broccoli cauliflower peas eggplant"

# get the user choice either vegetables or fruits
while True:
    user_choice= input('Enter Your choice\n enter "v"--> vegetables\n enter "f"--> fruits\n --------(v) or (f)------------->: ').lower()
    if user_choice.strip()== 'v' or user_choice.strip()== 'f':
        break
    else:
        print('Invalid Input.')
        continue 

# create a secret word
if user_choice.strip()== 'v':
    secret_word= random.choice(vegetables.split(' '))
else:
    secret_word= random.choice(fruits.split(' '))
# print(secret_word)
length_secret_word= len(secret_word)
tot_chances= length_secret_word +2 # give only 2 additional chances
