def toAthousand(x):  #this is the function to the answer of part one of Multiples where you use a for loop to get every odd integer from 0 to 1000.
    for count in range(0, x):
        if count is not count % 2 is 1:
            print count
toAthousand(1001) #this is the end to the function for the anwser of Multiples part one.

def fiveToAmil(z, y, i): #this is the function to the answer of part two of Multiples where you use a for loop to get every integer of multiples of 5 from 0 to 1000000.
    for i in range(i, z, y):
        if i <> 0:
            print i 
        else:
            continue
fiveToAmil(1000005, 5, 0) #this is the end to the function for the anwser of Multiples part two.

def sumList(a): #this is a function for the answer to the Sum List Section where you need to print the sum of all the values in a list.
    print a
    print sum(a)
sumList([1,2,5,10,255,3]) #this is the end to the function for the anwser of Sum List Section.

def avervageList(a): #this is a function for the answer to the Average List Section where you need find the average of the sum of all the values.
    count = 0
    while count < len(a):
        print count
        count += 1
    avervage = sum(a) / count
    print avervage    
avervageList([1,2,5,10,255,3]) #this is the end to the function for the anwser of Average List Section.
