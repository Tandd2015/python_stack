list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_one1 = [1,2,5,6,5]
list_two1 = [1,2,5,6,5,3]

list_one2 = [1,2,5,6,5,16]
list_two2 = [1,2,5,6,5]

list_one3 = ['celery','carrots','bread','milk']
list_two3 = ['celery','carrots','bread','cream']
# given assignment examples of two variables of which they are list type

def compareList(list_1, list_2): # this is the start of the function when passed two lists in it for comparision to determine if the lists are the same
    if len(list_1) <> len(list_2): #this is statement checks the lists by length to see if furthur arguements are needed to check each list
        print "the lists are not the same"
    else: # this is the start of the block of code that will check each list element versus each other out of both lists if both lists are the same size 
        for i in range(len(list_1)): # this is the begining of the foor loop that iterates the lists
            if list_1[i] != list_2[i]: 
                print "the lists are not the same"
                break
        else:
            print "the lists are the same" # this is the end booleans for the foor loop as well as the end of the foor loop

compareList(list_one, list_two) # this is the end of the function

def compareList1(list_1, list_2):
    if list_1 == list_2:
        print "The lists are the same"
    else:
        print "The lists are not the same"
compareList1(list_one2, list_two2) 