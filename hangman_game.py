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
    user_choice_print='vegetable'
    secret_word= random.choice(vegetables.split(' '))
else:
    user_choice_print='fruit'
    secret_word= random.choice(fruits.split(' '))
length_secret_word= len(secret_word)    # get the length of secret word 
tot_chances= length_secret_word +2      # give only 2 additional chances

# get user's inputs and check
print(f'You have to guess a {user_choice_print}.')
user_word=[]
user_word= ['_']*length_secret_word
#user_word= str(user_word)
print(user_word)

while True:
    guess_letter= input('Enter Your guess: ').strip()
    #print(guess_letter)
    if guess_letter in secret_word:
        #print(guess_letter)
        for i in range(length_secret_word):
            #print(1)
            if secret_word[i] == guess_letter:
                #user_word = list(user_word)
                user_word[i]= guess_letter
        #user_word= str(user_word)        
        print(user_word)
