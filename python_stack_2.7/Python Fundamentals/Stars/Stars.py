def draw_stars(arr): # beginning of function that passes an variable that is an array
    
    for value in arr: # foor loop to iterate the values of an array
        print value * "*" # print each value of and element within the arr multiplied by a string containing a character

x = [4, 6, 1, 3, 5, 7, 25] # variable with an array as a value
draw_stars(x) # end of the fucntion

def draw_stars1(arr): # beginning of function that passes an variable that is an array

    for value in arr: # foor loop to iterate the values of an array
        if isinstance(value, int): # a conditional with a function to determine whether an element in an array is a integer
            print value * "*" # print each value of and element within the arr multiplied by a string containing a character
        elif isinstance(value, str): # a conditional with a function to determine whether an element in an array is a string
            distance = len(value) # a variable with the value of a function to get a strings length
            worm = value[0].lower() # a variable with the value of a function to lower the case of a strings character letter
            print distance * worm # print two variables multiplied by each other
        else:
            print "Function does not currently support this type of Arguement"
x = [4, "TOM", 1, "Micheal", 5, 7, "Jimmy Smith",] # variable with an array as a value
draw_stars1(x) # end of the fucntion