import json 

x = {
    "name":"Srikanth",
    "age":18,
    "married":False,
    "Education":True,
    "Languages":('Tamil','English'),
    "pets":None,
    "cars":[
        {'model':'BMW 230',"mpg":27.5},
        {'model':'Audio R8',"mpg":24}
    ]
}

print(json.dumps(x, indent=4, separators=(".","="), sort_keys=True))