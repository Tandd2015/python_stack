class Call(object):
    NUM_CALLS = 0
    def __init__(self, caller, phone_num, reason):
        self.caller = caller
        self.phone_num = phone_num
        self.time_of_call = datetime.now()
        self.reason = reason
        self.id = Call.NUM_CALLS
        
        Call.NUM_CALLS += 1
    
    def display_info(self):
        print "\n" + ("#" * 20)
        for attr, val in self.__dict__.iteritems():
            if attr == "time_of_call":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)
        print "#" * 20

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = self.get_queue_size()

    def sort(self):
        for i in range(0, self.queue_size):
            for j in range(0, self.queue_size-i-1):
                if self.calls[j].call_time > self.calls[j+1].call_time:
                    self.calls[j], self.calls[j+1] = self.calls[j+1], self.calls[j]:
        return self

    def get_queue_size(self):
        return len(self.calls)

    def add(self, a_call):
        self.calls.append(a_call)

    def remove(self, r_call):
        self.calls.remove(r_call)

    def info(self):
        for call in self.calls:
            call.display_info()


'''
You can run this file to interactively add calls
'''


def handle_call():
    print "Would You like to make a call?"
    print "type [1] for yes and [0] for no"
    ans = raw_input()
    return int(ans)

def take_call():
    print "What is your name?"
    name = raw_input()
    print "What is your reason for calling?"
    reason = raw_input()
    print "Please confirm your phone number"
    num = raw_input()
    print "Please stay on the line while we proccess your call"
    return Call(name, num, reason)

game_on = True
center = CallCenter()
while game_on:
    ring = handle_call()
    if ring == 1:
        center.calls.append(take_call())
        print "All calls today:"
        center.info()
    else:
        game_on = False
# import turtle # imports turtle module to page
# wn = turtle.Screen() # sets a variable to open a draw screen for turtle 
# daniel = turtle.Turtle() # sets a variable to put a pionter on the screen to draw with
# daniel.shape('turtle') # sets tthe pionter used to draw to be an icon of a turtle


# DIST2 = 3 # the distance we want the pointer to travel each time
# for a in range(0,1):
#     daniel.right(60)
#     for b in range(0,36):
#         daniel.right(10)
#         daniel.backward(6)
# for c in range(0,6):  # first foor loop that will determine how many squares to draw
#     print "c", c # prints a string before and where the variable is currently at in the foor loop to the console
#     daniel.right(60)
#     for d in range(0,36):  # the second foor loop determine how to draw each square
#         print "d", d # prints a string before and where the variable is currently at in the foor loop to the console
#         daniel.right(10) # turn the pointer 90 degrees to the right
#         daniel.forward(6) # advance according to set distance
#     DIST2 += 3 # add to set distance

# DIST = 3 # the distance we want the pointer to travel each time
# for s in range(0, 1):
#     for c in range(0,36):
#         daniel.left(10)
#         daniel.forward(DIST)
# for ra in range(0,1):
#     daniel.left(60)
#     for b in range(0, 36):
#         daniel.right(10)
#         daniel.forward(DIST)
#     # for a in range(0, 36):
#     #     daniel.left(10)
#     #     daniel.forward(DIST)
#     # daniel.right(45)
#     daniel.left(90)

    
# for i in range(0,3): # first foor loop that will determine how many squares to draw
#     daniel.left(60)
#     for y in range(0,36): # the second foor loop determine how to draw each square
#         print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
#         daniel.left(10) # turn the pointer 90 degrees to the left
#         daniel.backward(DIST) # advance according to set distance
    # for z in range(0,360): # the second foor loop determine how to draw each square
    #     print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
    #     daniel.right(1) # turn the pointer 90 degrees to the left
    #     daniel.forward(DIST) # advance according to set distance
    # for z in range(0,360): # the second foor loop determine how to draw each square
    #     print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
    #     daniel.left(1) # turn the pointer 90 degrees to the left
    #     daniel.backward(DIST) # advance according to set distance
    # for a in range(0,360): # the second foor loop determine how to draw each square
    #     print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
    #     daniel.right(1) # turn the pointer 90 degrees to the left
    #     daniel.backward(DIST) # advance according to set distance
    # for b in range(0,360): # the second foor loop determine how to draw each square
    #     print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
    #     daniel.right(1) # turn the pointer 90 degrees to the left
    #     daniel.backward(DIST) # advance according to set distance
    # for c in range(0,360): # the second foor loop determine how to draw each square
    #     print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
    #     daniel.right(1) # turn the pointer 90 degrees to the left
    #     daniel.backward(DIST) # advance according to set distance
    # for d in range(0,360): # the second foor loop determine how to draw each square
    #     print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
    #     daniel.right(1) # turn the pointer 90 degrees to the left
    #     daniel.backward(DIST) # advance according to set distance
    

# DIST1 = 3 # the distance we want the pointer to travel each time
# for a in range(0,9):  # first foor loop that will determine how many squares to draw
#     print "a", a # prints a string before and where the variable is currently at in the foor loop to the console
#     for b in range(0,9):  # the second foor loop determine how to draw each square
#         print "b", b # prints a string before and where the variable is currently at in the foor loop to the console
#         daniel.right(72) # turn the pointer 90 degrees to the left
#         daniel.forward(DIST1) # advance according to set distance
#     DIST1 += 1 # add to set distance

# DIST2 = 3 # the distance we want the pointer to travel each time
# for x in range(0,9): # first foor loop that will determine how many squares to draw
#     print "x", x # prints a string before and where the variable is currently at in the foor loop to the console
#     for y in range(0,9): # the second foor loop determine how to draw each square
#         print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
#         daniel.left(36) # turn the pointer 90 degrees to the left
#         daniel.backward(DIST2) # advance according to set distance
#     DIST2 += 1 # add to set distance

# DIST3 = 3 # the distance we want the pointer to travel each time
# for x in range(0,9): # first foor loop that will determine how many squares to draw
#     print "x", x # prints a string before and where the variable is currently at in the foor loop to the console
#     for y in range(0,9): # the second foor loop determine how to draw each square
#         print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
#         daniel.right(72) # turn the pointer 90 degrees to the left
#         daniel.backward(DIST3) # advance according to set distance
#     DIST3 += 1 # add to set distance

# DIST4 = 3 # the distance we want the pointer to travel each time
# for x in range(0,36): # first foor loop that will determine how many squares to draw
#     print "x", x # prints a string before and where the variable is currently at in the foor loop to the console
#     for y in range(0,9): # the second foor loop determine how to draw each square
#         print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
#         daniel.left(36) # turn the pointer 90 degrees to the left
#         daniel.backward(DIST4) # advance according to set distance
#     DIST4 += 3 # add to set distance

# DIST5 = 3 # the distance we want the pointer to travel each time
# for x in range(0,36): # first foor loop that will determine how many squares to draw
#     print "x", x # prints a string before and where the variable is currently at in the foor loop to the console
#     for y in range(0,9): # the second foor loop determine how to draw each square
#         print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
#         daniel.left(36) # turn the pointer 90 degrees to the left
#         daniel.backward(DIST5) # advance according to set distance
#     DIST5 += 3 # add to set distance

# DIST6 = 3 # the distance we want the pointer to travel each time
# for x in range(0,36): # first foor loop that will determine how many squares to draw
#     print "x", x # prints a string before and where the variable is currently at in the foor loop to the console
#     for y in range(0,9): # the second foor loop determine how to draw each square
#         print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
#         daniel.left(36) # turn the pointer 90 degrees to the left
#         daniel.backward(DIST6) # advance according to set distance
#     DIST6 += 3 # add to set distance

# DIST7 = 3 # the distance we want the pointer to travel each time
# for x in range(0,36): # first foor loop that will determine how many squares to draw
#     print "x", x # prints a string before and where the variable is currently at in the foor loop to the console
#     for y in range(0,9): # the second foor loop determine how to draw each square
#         print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
#         daniel.left(36) # turn the pointer 90 degrees to the left
#         daniel.backward(DIST7) # advance according to set distance
#     DIST7 += 3 # add to set distance

# DIST8 = 3 # the distance we want the pointer to travel each time
# for x in range(0,36): # first foor loop that will determine how many squares to draw
#     print "x", x # prints a string before and where the variable is currently at in the foor loop to the console
#     for y in range(0,9): # the second foor loop determine how to draw each square
#         print "y", y # prints a string before and where the variable is currently at in the foor loop to the console
#         daniel.left(36) # turn the pointer 90 degrees to the left
#         daniel.backward(DIST8) # advance according to set distance
#     DIST8 += 3 # add to set distance

# DIST2 = 3 # the distance we want the pointer to travel each time
# for c in range(0,36):  # first foor loop that will determine how many squares to draw
#     print "c", c # prints a string before and where the variable is currently at in the foor loop to the console
#     for d in range(0,9):  # the second foor loop determine how to draw each square
#         print "d", d # prints a string before and where the variable is currently at in the foor loop to the console
#         daniel.right(36) # turn the pointer 90 degrees to the right
#         daniel.forward(DIST2) # advance according to set distance
#     DIST2 += 3 # add to set distance

# DIST3 = 3 # the distance we want the pointer to travel each time
# for e in range(0,6): # first foor loop that will determine how many squares to draw
#     print "e", e # prints a string before and where the variable is currently at in the foor loop to the console
#     for f in range(1,5):  # the second foor loop determine how to draw each square
#         print "f", f # prints a string before and where the variable is currently at in the foor loop to the console
#         daniel.right(360) # turn the pointer 90 degrees to the right
#         daniel.backward(DIST3) # advance according to set distance
#     DIST3 += 9 # add to set distance
wn.exitonclick() # exits drawing screen on click also allows the screen to stay open
