def newList(x):
    print x
    x.sort()
    print x
    first_list = x[:len(x)/2]
    print "first_list", first_list
    last_list = x[len(x)/2:]
    print "last_list_orginal", last_list
    last_list.insert(0, first_list)
    print "last_list_new", last_list
newList([19,2,54,-2,7,12,98,32,10,-3,6])