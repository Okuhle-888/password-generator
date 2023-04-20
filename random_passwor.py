import string
import random

def another_password():
    
    response = input(' what length would you like your password to be?')

    password_char = random.choice

    s1 ='ABCDEFGHIJKLmnopqrstuvwxyz '(string.ascii_letters) # contains all alphabets both in caps and lower case
    s2 ='12345678' (string.digits)
    s3 ='#$%&()_-+=><*?' (string.punctuation)

    # we are able to join beause they are the same type string

    all_charactors = s1+s2+s3   # cocantination


    list_of_all_characters = list (all_charactors)

    random.shuffle(list_of_all_characters)


    password = ''
    
    size = len(list_of_all_characters) - 1 

for x in range(response):
        # generate a random number between 0 and the size of all charactors

        num = random.randint(0,size)
        final_password = final_password + list_of_all_characters [num]



        print(f'{final_password}is your password of length {password_len}')

        another_password()


        password_gen()

       



