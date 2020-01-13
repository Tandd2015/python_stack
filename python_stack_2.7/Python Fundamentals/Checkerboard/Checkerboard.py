def printCheckerboard(): # this is the beginning to a function that will print a checkerboard pattern to the terminal 
    for k in range(0, 1): # this foor loop will run to act as if setting up a general area
        for k in range(0, 8): # this for loop will run 8 times to print what i want in each line on my general area
            if k % 2 is 0: # a conditional boolean that will print the desired line upon the general area depending on the value returned from it
                newStr = "{} {} {} {} " # new string
                print newStr.format('*', '*', '*', '*') # the values i want to pass into the string to print
            else:
                newStr1 = " {} {} {} {}" # new string
                print newStr1.format('*', '*', '*', '*') # the values i want to pass into the string to print
# printCheckerboard() # end of the function 

def CheckerBoard1(pattern_1, pattern_2):
    for board in range(0, 1):
        for board in range(0, 8):
            if board % 2 is 0:
                print pattern_1
            else:
                print pattern_2
CheckerBoard1('* %s' % '* %s' % '* %s' % '* ', ' *%s' % ' *%s' % ' *%s' % ' *')