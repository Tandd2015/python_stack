import random # import that random module into python
def scoresGrades(s): # beginning of function
    print "Scores and Grades"
    for i in range(0, s): # beginning of foor loop that will iterate through a variable
        # print i, s
        random_number = random.randint(60, 100) #a variable  with the value of a dynamically created random integer through a function
        #print random_number
        if random_number <= 69 and random_number >= 60: # conditional to determine  what string to print
            print "Score: {}; Your Grade is D".format(random_number) # printing with a function attached to it to update the string information
        elif random_number <= 79 and random_number >= 70: # conditional to determine  what string to print
            print "Score: {}; Your Grade is C".format(random_number) # printing with a function attached to it to update the string information
        elif random_number <= 89 and random_number >= 80: # conditional to determine  what string to print
            print "Scores: {}; Your Grade is B".format(random_number) # printing with a function attached to it to update the string information
        else: # conditional to determine  what string to print
            print "Score: {}; Your Grade is A".format(random_number) # printing with a function attached to it to update the string information
        
        if i + 1 == s:
            print "End of the program. Bye!"
scoresGrades(11) # calling the fucntion with an arguement

