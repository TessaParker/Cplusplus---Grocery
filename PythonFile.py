import re
import string
import os.path
from os import path


    # This function will be called if the user selects the first menu option
    # Print all items purchased and the quantity of each
def OptionOne():
    # open the item text
    text = open("items.txt", "r")
    frequency_dict = dict()
    #each line will be an item
    for line in text:
        item = line.strip()
        #populate/increment dictionary
        if item in frequency_dict:
            frequency_dict[item] = frequency_dict[item] + 1
        else:
            frequency_dict[item] = 1

    # iterate through dictionary and print for each item
    for key in frequency_dict.keys():
        print(key, ":", frequency_dict[key], "\n")
    #close the file
    text.close()

# This function will be called if menu option 2 is selected
# Prints individual item and frequency
def OptionTwo(v):
    # open item list
    text = open("items.txt", "r")
    # initialize item count to 0
    itemCount = 0

    for line in text:
        item = line.strip()
        # increment item count for each occurence of user item (v)
        if item == v:
            itemCount += 1

    # output the item and frequency
    print(v, ":", itemCount, "\n\n")
    #close the file
    text.close()

def OptionThree():
    #open item file to read
    text = open("items.txt", "r")
    #open frequency file to write
    data = open("frequency.txt", "w")
    #create empty dictionary
    frequency_dict = dict()
    #each line in file is an item
    for line in text:
        item = line.strip()
        #increment/populate dictionary
        if item in frequency_dict:
            frequency_dict[item] = frequency_dict[item] + 1
        else:
            frequency_dict[item] = 1
    #write each item and quantity to frequency file
    for key in frequency_dict.keys():
        data.write(str(key) + " " + str(frequency_dict[key]) + "\n")
    #close files after reading/writing
    text.close()
    data.close()


# Test function for item file
def testFile():
    print("Testing File:\n")
    text = open("items.txt", "r")
    itemRead = text.read()
    print(itemRead)
    text.close()