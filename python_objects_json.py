import json

print(json.dumps({'name':'srikanth','age':28}))   #dictionary
print(json.dumps(['srikanth','28']))            #list
print(json.dumps(('srikanth','28')))   #tuple
print(json.dumps("Hello"))   
print(json.dumps(33))
print(json.dumps(44.5))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))