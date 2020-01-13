import random
def randInt(min=0 ,max=100):
    if(min>max and max>0):
        num=round(random.random()*(min-min+2)+min-1)
    elif(max<0):
        num=round(random.random()*(max-max+2)+max-1)
    else:
        num=round(random.random()*(max-min)+min)
    return num

print(randInt())	    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
print(randInt(min=50, max=5)) 
print(randInt(min=-6, max=-4))
print(randInt(min=-2, max=-4)) 

