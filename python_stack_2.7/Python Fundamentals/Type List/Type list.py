serpent = ['kingCobras',2015,'viper',1988.369,'PYTHON','rattleSnake']
leviathan = ['anaconda','komodoDragon','Raptor']
basilisk = [1900,1408.369,2000,2010,2020.963]
# this is a list of variables to pass through the function
def slither(nessy): #this is the start of the function that will find the type of each element within the variable and then sort each into a new variable depending on which type each is.
    megalodon = ""
    annunaki = 0 # two new variables to sort the passed variable into by type of element
       
    for count in nessy: # this is the start of the foorloop that will cycle the elements of the variables
        if isinstance(count, int) or isinstance(count, float):
            annunaki += count
        elif isinstance(count, str):
            megalodon += ' ' + count # this is the end of the block of code to cycle through the variables elements
    if megalodon and annunaki: # this is the start to the block of code that will print what type of list each variable is along with sorted new variables with the corrosponding elements of that type from the old variable.
        print "This list you entered is a mixed list"
        print "Megalodon:", megalodon
        print "Annunaki:", annunaki
    elif megalodon:
        print "This list you entered is a string list"
        print "Megalodon:", megalodon
    else:
        print "This list you entered is integer or float list"
        print "Annunaki:", annunaki # this is the end of the block of code that prints the information found while running the function
slither(leviathan) # this is the end of the function