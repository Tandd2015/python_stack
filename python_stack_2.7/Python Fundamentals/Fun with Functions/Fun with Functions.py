def odd_even(x): # beginning of function
    for i in range(x+1): # a foor loop to cycle through 0 to 2001 excluding 2001
        # print i
        if i % 2 == 0: # a conditional statement to determine if the number is even 
            Str = "Number is {}. This is an even number".format(i) # a variable set to a string with a function attached to it to up date each loop
            print Str
        else: # a conditional statement to determine if the number is not even (if not even there for odd)
            Str1 = "Number is " + str(i) + ". This is an odd number"
            # Str1 = "Number is {}. This is an odd number".format(i) # a variable set to a string with a function attached to it to up date each loop
            print Str1
odd_even(2000) # function call with arguement to be passed

def multiply(list, num): # beginning of function
    for o in range(len(list)): # a foor loop to cycle through list length
        # print o
        list[o] *= num # mulitplies every element in the list by a number
        # print list
    return list # returns list
a = [2,4,10,16] # variable with a list as a value
b = multiply(a, 5) # variable with a function that passes a variable and a arguement
print b

def layered_multiples(arr): # beginning of function
    new_array = [] # a new blank array
    #print arr
    for val in arr: # first foor loop to cycle through the values of the arr
        # print val
        val_arr = [] # a new blank array
        for i in range(0, val): # second foor loop to cycle throught the range of each element
            # print i
            val_arr.append(1) # append one to val_arr every time the foor loop is executed
            #print val_arr
        new_array.append(val_arr)  # append each val_arr to new_array for every time the first foor loop is executed
    return new_array # returns a new_array as the value of the function
x = layered_multiples(multiply([2,4,5],3)) # variable with a multi-layered function as the value
print x

