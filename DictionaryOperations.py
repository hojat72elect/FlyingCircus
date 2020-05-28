"""What we can do to our Dictionaries in python"""

simpleDict = {"Canada": "Ottawa", "USA": "Washington", "Germany": "Berlin", "Russia": "Moscow",
              "Uruguay": "Montevideo", "dominican republic": "Santo Domingo"}

print(f'my dict is: {simpleDict}')
print(len(simpleDict))
print(simpleDict["Germany"])
simpleDict["Canada"] = "the sweet and lovely city of Ottawa"
print(simpleDict, end='\n\n')

for key in simpleDict.keys():
    print(key)
print()

for country, capital in simpleDict.items():
    print(f'{capital} is the capital of {country}', end='\n\n')

del simpleDict["Canada"]
print(f'unfortunately, the Canada was removed: {simpleDict}', end='\n\n')

print("Germany" in simpleDict)
print("Iran" in simpleDict, end='\n\n')

simpleDict.update({"Israel": "Jerusalem", "Armenia": "Yerevan"},
                  Mexico="New Mexico", Iraq="Baghdad")  # an excellent way to update our dictionaries.
print(simpleDict)
