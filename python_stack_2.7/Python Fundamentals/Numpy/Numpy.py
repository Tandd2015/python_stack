def libraryRequest(): # beginning of function that returns a variable from request module
    import json # imports json language
    import requests # imports requests module
    t = requests.request('get', 'http://pokeapi.salestock.net/api/v2/pokemon/') # variable with requests module to execute a get call to an api
    json_data = json.loads(t.text)
    print json_data
    for count in range(json_data[u'count']): # foor loop to cycle through the count dictionary and create a varialble count
        print count
libraryRequest() # executes a function call