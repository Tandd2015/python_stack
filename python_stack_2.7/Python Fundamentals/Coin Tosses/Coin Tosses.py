import random # importing the random module

def coinTosses(finger_strength): # beginning of function with a variable to pass through
    greater_than = 0 # a variable for the random.unifrom function in the value of a variable
    less_than = 1 # a variable for the random.unifrom function in the value of a variable
    digits = int(0) # a variable for the round(random.unifrom) function in the value of a variable
    flip_counter = 1 # a variable to count total iterations
    heads_counter = 0 # a variable to count conditional statement that is exicuted
    tails_counter = 0 # a variable to count conditional statement that is exicuted
    for flips in range(1, finger_strength + 1): # beginning of foor loop to iterate finger_strength
        quarter = round(random.uniform(greater_than,less_than), digits) # a variable with a multilayered function as a value
        flips = quarter # a variable set to the value of another variable
        # print flips, flip_counter
        if flips > 0 and flip_counter != finger_strength: # condtional to determine which block of code to run 
            heads_counter += 1 # a variable to count conditional statement that is exicuted
            heads = "head!" # a new variable with a string for value
            print "Attempt #{}:".format(flip_counter), " Throwing a coin... It's a", heads, "... Got", heads_counter, "head(s) so far and", tails_counter, "tail(s) so far"
        elif flips == 0 and flip_counter != finger_strength: # condtional to determine which block of code to run
            tails_counter += 1 # a variable to count conditional statement that is exicuted
            tails = "tail!" # a new variable with a string for value
            print "Attempt #{}:".format(flip_counter), " Throwing a coin... It's a", tails, "... Got", heads_counter, "head(s) so far and", tails_counter, "tail(s) so far"
        elif flips > 0 and flip_counter == finger_strength:
            heads_counter += 1 # a variable to count conditional statement that is exicuted
            heads = "head!" # a new variable with a string for value
            print "..."
            print "Attempt #{}:".format(flip_counter), " Throwing a coin... It's a", heads, "... Got", heads_counter, "head(s) so far and", tails_counter, "tail(s) so far"
            print "Ending the Program, thank you!"
        else:
            tails_counter += 1 # a variable to count conditional statement that is exicuted
            tails = "tail!" # a new variable with a string for value
            print "..."
            print "Attempt #{}:".format(flip_counter), " Throwing a coin... It's a", tails, "... Got", heads_counter, "head(s) so far and", tails_counter, "tail(s) so far"   
            print "Ending the Program, thank you!"
        flip_counter += 1 # a variable to count total iterations

coinTosses(5000) # end of the function