import json
import time
from difflib import get_close_matches

dictionary = json.load(open("data.json","r")) #Importing JSON file with the data
def find_word(word_key): #Finding the word which takes the role of key in dictionary
    return dictionary[word_key]


def check_key(checkable_key):
    if checkable_key in dictionary:
        return find_word(checkable_key)
    elif checkable_key.title() in dictionary: #Checking the word with the .title()
        return dictionary[checkable_key.title()]
    elif checkable_key.upper() in dictionary:#Checking the word with the .upper()
        return dictionary[checkable_key.upper()]
    elif checkable_key == "/quit":#Quiting the program
        print("Quitting...")
        time.sleep(2)
        exit()

    elif len(get_close_matches(checkable_key, dictionary.keys())) > 0: #Finding the same key
        yes_no = input("Did you mean %s. Enter Y if yes and N if no." % get_close_matches(checkable_key, dictionary.keys())[0]).upper()
        if yes_no == "Y":
            return dictionary[get_close_matches(checkable_key, dictionary.keys())[0]]
        elif yes_no == "N":
            return "The word doens exist"
    else:
        return "The word doens exist.Please check the word one more time!"


while True:
    word = input("Enter the word: ")#Entering the word
    output = check_key(word.lower()) #The output of the program
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
