def libraryRequest(): # beginning of function that returns a variable from request module
    import json # imports json language
    import requests # imports requests module
    t = requests.request('get', 'http://pokeapi.salestock.net/api/v2/pokemon/') # variable with requests module to execute a get call to an api
    json_data = json.loads(t.text)
    # print json_data
    for count in range(1, json_data[u'count'] + 1): # foor loop to cycle through the count dictionary and create a varialble count
        # print count
        req_pokeball = "I have caught all {} pokemon in this PokeAPI index.".format(count) # a variable with a string and a function to ammend the string
    #print req_pokeball
    charizard = json_data[u'results'][5][u'name'] # a variable with the name of a pokemon from the json data
    blastiose = json_data[u'results'][8][u'name'] # a variable with the name of a pokemon from the json data
    venusaur = json_data[u'results'][2][u'name'] # a variable with the name of a pokemon from the json data
    #print charizard, blastiose, venusaur
    topThree = "My top three are {}, {}, and last but not least my fav {}".format(venusaur, blastiose, charizard) # a variable with a string and a function to ammend the string with muliple variables
    #print topThree
    theAnswer = req_pokeball + " " + topThree # a variable concatinating two variables into a string
    print theAnswer # prints a variable 
    return theAnswer # returns a variable
libraryRequest() # executes a function call