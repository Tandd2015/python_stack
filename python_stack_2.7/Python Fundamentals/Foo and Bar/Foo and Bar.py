def fooBar(): # beginning of the function THAT DOES NOT FUNCTION PROPERLY
    for idx in range(1, 100001): # beginning of the foor loop that will cycle through all of the numbers
        prime = True # variable for prime
        perfect_4 = False # variable for perfect square
        for check in range(2, idx + 1): # nested foor loop that will cycle a check for each idx number
            if idx % check == 0 and check != idx: # a conditional  that will check to see if the number is prime
                prime = False # changes the value of the variable 
            if idx // check == check: # a conditional that will check to see if the number is a perfect square
                perfect_4 = True # changes the value of the variable
        if prime is True: # a conditional that will print for prime numbers
            print 'Foo'
        elif perfect_4 is True: # a conditional that will print for perfect square numbers
            print 'Bar'
        else: # a conditional that will print for neither perfect square or prime numbers
            print 'FooBar'
# fooBar() # end of function
def foo_and_bar(start, finish):# THIS FUNCTION WORKS PROPERLY
    for index in range(start, finish + 1):
        prime_indicator = True
        perfect_square_indicator = False
        if index is 1:
            prime_indicator = False
            perfect_square_indicator = False
        else:
            for nested_index in range(2, index + 1):
                if index % nested_index == 0 and index <> 1 and nested_index <> index:
                    prime_indicator = False
                if index == nested_index * nested_index:
                    perfect_square_indicator = True
        if prime_indicator is True:
            print 'Foo'
        elif perfect_square_indicator is True:
            print 'Bar'
        else:
            print 'FooBar'
foo_and_bar(100, 100000)