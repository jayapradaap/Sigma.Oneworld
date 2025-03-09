import json
'''
#Must Know the differences between the json.load(),json.loads()
#Also must know the difference between the json.dump(),json.dumps()
#We should understand above concepts before playing with JSON in python.

#loading a json string format data into a variable and printing it:
mystring='{"country":"india","languages":"Tamil"}'
my_dict=json.loads(mystring)
print("Lets see the Dicrionary from the Json file :")
print(my_dict)
print("The Languages are :")
print(my_dict['languages'])

#Loading a json file data into a python variable and printing it:
with open("data.json") as file:
    data = json.load(file)

print(data)

mydict1 = {
            "country":"india",
            "languages":"Tamil",
            "age":"22"
          }

#Dumping a python object into a file in a json format:
my_dict2 = json.dumps(mydict1)
print(my_dict2)

json_file =  open("person.txt","w")
json.dump(mydict1,json_file)

'''
#Loading a json file data into a variable and dumping them in json string format :
with open("data.json") as my_data:
    my_file = json.load(my_data)

print(json.dumps(my_file,indent=4, sort_keys=False))