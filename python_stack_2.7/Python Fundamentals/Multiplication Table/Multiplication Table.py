def multiplicity(x, y): #beginning of function where x and y is passed into for multiplication table
    print "My Mutlipication Table:"
    for vertical in xrange(0, x + 1): # a for loop to run through the range of x and to setup vertical variable
        if vertical is 0: # conditional testing and replacing any mutiplications of zero for the vertical variable
            vertical = vertical + 1
        for horizontal in xrange(0, y + 1): #a nested foor loop to get the range of y and to setup the horizontal variable
            if horizontal is 0: # conditional testing and replacing any mutiplications of zero for the vertical variable
                horizontal = horizontal + 1
            print vertical * horizontal, "\t",
        print # printing the multiplication table in a horizontal tab
        # end of function 
# multiplicity(12, 12) # calling function and passing parameters into the variables of x and y.

def multiplication1(l, r):
    count = 0
    line = 0
    for hori in xrange(0, l + 1):
        if hori == 0:
            hori += 1
        for vert in xrange(0, r + 1):
            if vert == 0:
                vert += 1
            if hori == 1 and vert == 1:
                if count == 0:
                    line = 'x'
                    count += 1
                else: 
                    line = hori * vert
                    count += 1
            else:
                line = hori * vert
            print line, "\t", 
        print
multiplication1(12, 12)