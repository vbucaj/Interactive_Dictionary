import json
from difflib import SequenceMatcher as sm
from difflib import get_close_matches as gcm

#reading the data

data=json.load(open('data.json'))
#global variables
ct=0
ct1=0
ct2=0
ct3=0
ct4=0

#Helping functions
def yes_no_2(yes_no):
    global ct3,ct4
    if yes_no=='yes':
        print('The definition of {} is: '.format(candidates[1].upper()))
        return data[candidates[1]]
    elif yes_no=='no':
        ct4+=1
        if ct4==3:
            return "The input is incorrect. The program will terminate now!"
        else:
            word=input("No such word exists. Please enter another word: ")
            return word_def(word)
    else:
        ct3+=1
        if ct3==3:
            return "The input is incorrect. The program will terminate now!"
        else:
            yn=input("The input is invalid. Please enter {} or {}: ".format('YES', 'NO')).lower()
            return yes_no_2(yn)

def yes_no_f(yes_no):
    global ct, ct1,ct2,ct3
    if yes_no =='yes':
        print('The definition of {} is: '.format(candidates[0].upper()))
        return data[candidates[0]]
    elif yes_no=='no':
        ct+=1
        if len(candidates)>1:
            yes_no=input("Did you mean {} instead? Enter 'yes' or 'no': ".format(candidates[1].upper())).lower()
            return yes_no_2(yes_no)

        if ct==3:
            return "The word entered cannot be found. The program will terminate now!"
        else:
            word=input("Please enter the word again: ")
        return word_def(word)
    else:
        ct2+=1
        if ct2==3:
            return "The input is incorrect. The program will terminate now!"
        else:
            yn=input("The input is invalid. Please enter {} or {}: ".format('YES', 'NO')).lower()
            return yes_no_f(yn)

#Main function

def word_def(key):
    global ct, ct1,candidates
    if key.lower() in data.keys():
        print("The definition of {} is: ".format(key.upper()))
        return data[key.lower()]
    elif key.title() in data.keys():
        print('The definition of {} is: '.format(key.upper()))
        return data[key.title()]
    elif key.upper() in data.keys():
        print('The definition of {} is: '.format(key.upper()))
        return data[key.upper()]
    elif len(gcm(key.lower(),data.keys(),cutoff=0.8))>0:
        candidates=gcm(key.lower(),data.keys(),cutoff=0.8)

        yes_no=input("Did you mean {} instead? Enter 'yes' or 'no': ".format(candidates[0].upper())).lower()

        return yes_no_f(yes_no)

    elif len(gcm(key.lower(),data.keys(),cutoff=0.8))==0:
        ct1+=1
        word=input("No such word exists. Please try again: ")
        if ct1==3:
            return "The word entered cannot be found. The program will terminate now!"
        return word_def(word)



# Prompting the user to enter the word whose definition they want
key=input("Enter word: ")

output=word_def(key)


#printing out the definition(s)
if type(output)== list:
    i=0
    for item in output:
        i+=1
        print('{}. {}'.format(i,item))
else:
    print(output)
