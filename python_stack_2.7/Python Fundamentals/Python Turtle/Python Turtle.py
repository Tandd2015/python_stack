import turtle # imports turtle module to page
wn = turtle.Screen() # sets a variable to open a draw screen for turtle 
daniel = turtle.Turtle() # sets a variable to put a pionter on the screen to draw with
daniel.shape('turtle') # sets tthe pionter used to draw to be an icon of a turtle

DIST = 8 # the distance we want the pointer to travel each time
for x in range(0,8): # first foor loop that will determine how many squares to draw
    print "x", x # prints a string before and where the variable is currently at in the foor loop to the console
    for y in range(1,5): # the second foor loop determine how to draw each square
        print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
        daniel.left(80) # turn the pointer 80 degrees to the left
        daniel.backward(DIST) # advance according to set distance
    DIST += 6 # add to set distance

DIST1 = 8 # the distance we want the pointer to travel each time
for a in range(0,8):  # first foor loop that will determine how many squares to draw
    print "a", a # prints a string before and where the variable is currently at in the foor loop to the console
    for b in range(1,5):  # the second foor loop determine how to draw each square
        print "b", b # prints a string before and where the variable is currently at in the foor loop to the console
        daniel.left(80) # turn the pointer 80 degrees to the left
        daniel.forward(DIST1) # advance according to set distance
    DIST1 += 6 # add to set distance

DIST2 = 8 # the distance we want the pointer to travel each time
for c in range(0,8):  # first foor loop that will determine how many squares to draw
    print "c", c # prints a string before and where the variable is currently at in the foor loop to the console
    for d in range(1,5):  # the second foor loop determine how to draw each square
        print "d", d # prints a string before and where the variable is currently at in the foor loop to the console
        daniel.right(80) # turn the pointer 80 degrees to the right
        daniel.forward(DIST2) # advance according to set distance
    DIST2 += 6 # add to set distance

DIST3 = 8 # the distance we want the pointer to travel each time
for e in range(0,8): # first foor loop that will determine how many squares to draw
    print "e", e # prints a string before and where the variable is currently at in the foor loop to the console
    for f in range(1,5):  # the second foor loop determine how to draw each square
        print "f", f # prints a string before and where the variable is currently at in the foor loop to the console
        daniel.right(80) # turn the pointer 80 degrees to the right
        daniel.backward(DIST3) # advance according to set distance
    DIST3 += 6 # add to set distance
wn.exitonclick() # exits drawing screen on click also allows the screen to stay open
