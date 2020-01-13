def basic(end):
    for idx in range(end+1):
        print(idx)
# basic(150)

def multiples_of_five(start,end,increase):
    for idx in range(start,end+increase,increase):
        print(idx)
# multiples_of_five(5,1000,5)

def counting_the_dojo_way(start,end):
    for idx in range(start,end+start):
        if idx%10==0:
            print("Coding Dojo")
        elif idx%5==0:
            print("Coding")
        else:
            print(idx)
# counting_the_dojo_way(1,100)

def whoa_that_suckers_huge(start,end,increase):
    idx_sum=1
    for idx in range(start,end,increase):
        idx_sum+=idx
    print(idx_sum)
# whoa_that_suckers_huge(3,500000,2)

def countdown_by_fours(start,end,decrease):
    for idx in range(start,end,decrease):
        print(idx)
# countdown_by_fours(2018,1,-4)

def flexible_counter(lowNum,highNum,mult):
    for lowNum in range(highNum+1):
        if lowNum%mult==0 and lowNum!=0:
            print(lowNum)
# flexible_counter(2,9,3)
