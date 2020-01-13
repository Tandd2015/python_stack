def countdown(input):
    new_list= []
    for idx in range(input,-1,-1):
        new_list.append(idx)
    # print(new_list)
    return new_list
countdown(5)

def print_and_return(t_list):
    for idx in range(len(t_list)):
        if t_list[idx]==t_list[0]:
            print (t_list[idx])
        elif t_list[idx]==t_list[0+1]:
            return t_list[idx]
print_and_return([1,2])

def first_plus_length(tl):
    # print(tl[0]+len(tl))
    return tl[0]+len(tl)
first_plus_length([1,2,3,4,5])

def values_greater_than_second(tl1):
    new_list= []
    count= 0
    if len(tl1) < 2:
        return False
    else:
        for idx in range(len(tl1)):
            if tl1[idx]>tl1[1]:
                new_list.append(tl1[idx])
                count+=1
    print(count)
    return new_list
values_greater_than_second([5,2,3,2,1,4])
values_greater_than_second([3])

def length_and_value(size,value):
    new_list=[]
    for idx in range(0,size):
        new_list.append(value)
    return new_list, print(new_list)
length_and_value(4,7)
length_and_value(6,2)