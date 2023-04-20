import string  #to be able to use string properties we must 1st import them, "fetch"

import random  #we also use random properties

 

def anotherPassword():

    response = input("Do you want to generate another password (y/n)? ")

    if (response == "y"):

        passwordGen()

       

def passwordGen():

    passwordLen = int(input('How long do you want your password to be: '))

    alphabets = string.ascii_letters    #contains all the alphabets in both caps and lower case

    digits = string.digits              #contains all the digits

    punctuations = string.punctuation   #contains all the punctuatins

 

    #we are able to join the above variable because the are of the same type, string

    allCharactors = alphabets + digits + punctuations #this is called concantination

 

    #since the charactors are now one word we want to separate into a list of charactors that we can access one by one

    listOfCharactors = list(allCharactors) 

    #The list is ordered based on how they were added together, we have to jumble them before use

    random.shuffle(listOfCharactors)

    finalPassword = "" #this will be the users' password

   

    size = len(listOfCharactors) - 1 #index start at 0 hence -1

   

    for x in range(passwordLen):

        #generate a random number between 0 and the size of all charactors

        num = random.randint(0,size)

        finalPassword = finalPassword + listOfCharactors[num]

       

    print(f'{finalPassword} is your password of lenght {passwordLen}')

    anotherPassword()

   

passwordGen()

