def biggie_size(lis1):
    for idx in range(len(lis1)):
        if lis1[idx]>0:
            lis1[idx]="big"
    # print(lis1)
    return lis1
# biggie_size([-1,3,5,-5])

def count_positives(lis2):
    count= 0
    for idx in range(len(lis2)):
        if lis2[idx]>0:
            count+=1
    lis2[len(lis2)-1]= count
    # print(lis2)
    return lis2
# count_positives([-1,1,1,1])
# count_positives([1,6,-4,-2,-7,-2])

def sum_total(lis3):
    sum= 0
    for idx in range(len(lis3)):
        sum+=lis3[idx]
    # print(sum)
    return sum
# sum_total([1,2,3,4])
# sum_total([6,3,-2])

def average(lis4):
    avg= 0
    for idx in range(len(lis4)):
        avg+=lis4[idx]
    avg=avg/len(lis4)
    # print(avg)
    return avg
# average([1,2,3,4])

def length(lis5):
    count= 0
    for idx in lis5:
        count+=1
    print(count)
    return count
# length([37,2,1,-9])
# length([])

def minimum(lis6):
    if lis6==[]:
        return False, print (False)
    else:
        min_num=lis6[0]
        for idx in range(len(lis6)):
            if lis6[idx]<min_num:
                min_num=lis6[idx]
        return min_num
# minimum([37,2,1,-9])
# minimum([])

def maximum(lis7):
    if lis7==[]:
        return False, print (False)
    else:
        max_num=lis7[0]
        for idx in range(len(lis7)):
            if lis7[idx]>max_num:
                max_num=lis7[idx]
        return max_num
# maximum([37,2,1,-9])
# maximum([])

def ultimate_analysis(lis8):
    ua={
        'sumTotal': sum_total(lis8),
        'average': average(lis8),
        'minimum': minimum(lis8),
        'maximum': maximum(lis8),
        'length': length(lis8) 
    }
    return ua
# ultimate_analysis([37,2,1,-9])

def reverse_list(lis9):
    for idx in range(int(len(lis9)/2)):
        temp=lis9[idx]
        lis9[idx]=lis9[len(lis9)-1-idx]
        lis9[len(lis9)-1-idx]=temp
    return lis9
# reverse_list([37,2,1,-9])

