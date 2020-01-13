bio = {} # a variable with the value as a blank dictionary
bio["Name"] = "Daniel Duane Beatty Jr." # a key and value pair created to the blank dictionary variable
bio["Age"] = "30" # a key and value pair created to the blank dictionary variable
bio["country of birth"] = "United States Of America" # a key and value pair created to the blank dictionary variable
bio["Favorite Language"] = "Python" # a key and value pair created to the blank dictionary variable
def reading_makingDicts(dict): # beginning of function that passes a dictionary type variable to print a string
    #print dict
    for key, data in dict.iteritems():# foor loop to itertate through the dictionary keys and values
        print "My " + key + " is " + data # prints a sequence of strings and the key/value pairs
reading_makingDicts(bio) # end of function

bio_info = {} # a variable with the value as a blank dictionary
bio_info["name"] = "Daniel Beatty" # a key and value pair created to the blank dictionary variable
bio_info["age"] = "30" # a key and value pair created to the blank dictionary variable
bio_info["country of birth"] = "USA" # a key and value pair created to the blank dictionary variable
bio_info["favorite language"] = "Python" # a key and value pair created to the blank dictionary variable

def reading_makingDicts2(dict): # beginning of function that passes a dictionary type variable to print a string
    
    for key, data in dict.iteritems(): # foor loop to itertate through the dictionary keys and values
        part1 = "My {}".format(key) # a variable with a string and a function to ammend the string with the key of the dictionary every time the foor loop is executed
        part2 = " is {}".format(data)  # a variable with a string and a function to ammend the string with the value of the dictionary every time the foor loop is executed
        finish = part1 + part2 # a variable adding two different variables
        print finish # prints a variable

reading_makingDicts2(bio_info) # end of function