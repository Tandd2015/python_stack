practice_list = ['hello','world','my','name','is','Anna']
# a variable up above to pass through the function
def findCharacters(word_list, char): # the beginning to a function to search through a list of strings for a character in the word then to create a new string and print it of the variables that match the anwser to the boolean
    new_list = [] #new list to append variable values into
    for i in range(len(word_list)): #beginning to the foor loop that will iterate the variable
        if word_list[i].find(char) != - 1: # testing each value in the list for a condition of a particular character 
            new_list.append(word_list[i]) #appending the new list with the values that fit the condition of having char in it
    print new_list #end of function
findCharacters(practice_list, 'o') # pass variables into function here and calling the function 