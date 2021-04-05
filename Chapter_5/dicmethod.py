myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'},
    1: 2
}
# Dictionary Methods
print(myDict["fast"])
print(list(myDict.keys())) # Prints the keys of the dictionary
print(list(myDict.values())) # Prints the keys of the dictionary 
print(myDict.get("num")) # (num) is not present in myDict so returns none
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "name" : "tipu",
    "fruit" : "apple",
    "fruit1" : "banana",
    "myPC" : 'Asus vivo book pro',
}

myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("harry")) # Prints value associated with key "harry"
print(myDict["harry"]) # Prints value associated with key "harry"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("harry2")) # Returns None as harry2 is not present in the dictionary
print(myDict["harry2"]) # throws an error as harry2 is not present in the dictionary