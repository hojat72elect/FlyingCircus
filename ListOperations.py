"""This is a collection of good things we can do with our lists."""

countryList = ["Canada", "Germany", "Russia", "USA", "China"]

print(f'the length of the list is: {len(countryList)}')

for country in countryList:
    print(country)
print()

countryList.append("Ghana")
print(f'now the list is this:{countryList}', end='\n\n')

countryList.sort()  # by default, it sorts alphabetically but you can define lambdas to do custom sorting.
print(f'the sorted list is this: {countryList}', end='\n\n')

del countryList[-1]
print(f'so we deleted USA: {countryList}', end='\n\n')

print("Iran" in countryList)
print(countryList.__contains__("Canada"), end='\n\n')

AnotherCountryList = countryList.copy()  # makes a shallow copy of the list
AnotherCountryList.clear()

print(countryList.count("Ghana"), end='\n\n')

countryList.extend(("Brazil", "Dominican Republic"))  # notice that the iterable I gave to this function was a tuple.
print(f'the extended country list is this: {countryList}', end='\n\n')

countryList.reverse()
print(f'And now, we have the reversed version of our country list: {countryList}', end='\n\n')

'''This represents how easily we can do list comprehension in python: '''
firstList = [8, 3, 9, 4, 7, 3, 9, 8, 6, 3, 3, 9, 8, 6, 3]
secondList = [i ** 2 for i in firstList if i >= 6]
print(secondList)
