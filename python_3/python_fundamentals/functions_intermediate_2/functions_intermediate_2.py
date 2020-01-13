#--------- 1.Update Values in Dictionaries and Lists ---------
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#- 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
def list_of_lists_1(lol):
    for idx in range(len(lol)):
        # print(idx,lol[idx])
        for i in range(len(lol[idx])):
            # print(idx,i,lol[idx][i])
            if(lol[idx][i]==lol[1][0]):
                lol[idx][i]=15
    return lol, print(lol)
# list_of_lists_1(x)

#- 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
def list_of_dicts_1(lod):
    for idx in range(len(lod)):
        # print(idx, lod[idx])
        for k in lod[idx]:
            # print(idx,k,lod[idx]['last_name'])
            if lod[idx][k]==lod[0]['last_name']:
                lod[idx]['last_name']="Bryant"
    return lod, print(lod)
# list_of_dicts_1(students)

#- 3. In the sports_directory, change 'Messi' to 'Andres'
def dict_of_lists_1(dol):
    for idx in sports_directory:
        # print(idx)
        for i in range(len(sports_directory[idx])):
            # print(i,sports_directory[idx][i])
            if sports_directory[idx][i]==sports_directory['soccer'][0]:
                sports_directory[idx][i]="Andres"
    return dol, print(dol)
# dict_of_lists_1(sports_directory)

#- 4. Change the value 20 in z to 30
def list_of_dicts_2(lod):
    for idx in range(len(lod)):
        # print(idx, lod[idx])
        for i in lod[idx]:
            # print(idx,i,lod[idx][i])
            if lod[idx][i]==lod[idx]['y']:
                lod[idx][i]=30
    return lod, print(lod)
# list_of_dicts_2(z)

#--------- 2.1Iterate Through a List of Dictionaries ---------
students1 = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
#--iterateDictionary(students) 

#---Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
def iterateDictionary1(some_list):
    count=0
    stringer=""
    for idx in range(len(some_list)):
        count=len(some_list[idx])
        for i in some_list[idx]:
            stringer+=f"{i} - {some_list[idx][i]}, "
            count+=1
            if(count<len(some_list[idx])):
                if idx==len(some_list)-1:
                    stringer = stringer[:len(stringer) - 2]
                stringer+="\n"
            else:
                count=0
    print(stringer)
# iterateDictionary1(students1)

#--------- 3.Get Values From a List of Dictionaries ---------
def iterateDictionary2(key_name,some_list):
    for idx in range(len(some_list)):
        for i in some_list[idx]:
            if some_list[idx][i]==some_list[idx][key_name]:
                print(some_list[idx][i])
    return some_list
# iterateDictionary2('first_name',students1)
# iterateDictionary2('last_name',students1)

#--------- 4.Iterate Through a Dictionary with List Values ---------
#--- Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)

def printInfo(some_dict):
    for idx in some_dict:
        print (f"{len(some_dict[idx])} {idx.upper()}")
        for i in some_dict[idx]:
            print (i)
        print("\n")
    return some_dict
# printInfo(dojo)
