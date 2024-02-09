'''
Prompt user for new or existing notes
Show Notes
Allow for selection
Write to file and save
'''
import os
input("Select an option: ")


while True:
 print("New Note")
 print("See existing notes")
 print('Exit')
 
x = int(input())
if x == 1:
    # open file
with open('testFile.txt', "a") as file:

    

# set a list of lines to add:
lines = []
# write to file and add a seperator
file.writelines(s + '/n' for s in lines)
    
#open adn read the file after the appending:
with open("testFile.txt", "r") as file:
    print(file.read())