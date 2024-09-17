# Dictionary can store multiple data in key value pair
myDict={
    "keys":"values",
    "name":"Neeraj Singh Negi",
    "email":"nnn12345@gmail.com",
    "mobile":"21342345"
}
print(type(myDict))
print(myDict)

for keys in myDict:
    print(keys,myDict[keys])

print(myDict.get("email"))


myDict["name"]="Adarsh"
print(myDict)