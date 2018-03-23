### Creating lists

# Hard coded list
europe = ["Portugal", "Spain", "France", "UK", "Germany"]
print(europe)

# Appending
south_america = []
south_america.append("Brazil")
south_america.append("Peru")
south_america.append("Colombia")
south_america.append("Chile")
south_america.append("Argentina")
print(south_america)

# From string splitting
north_america = "Canada,United States,Mexico".split(",")
print(north_america)

# range function
numbers = list(range(10))           # [ 0, 10)
numbers = list(range(-5, 15))       # [-5, 15)
numbers = list(range(-5, 15, 4))    # [-5, 15) at intervals of 4
print(numbers)


print()
### Concatenation of lists

all_countries = europe + south_america + north_america
print(all_countries)


print()
### Sorting lists

# Strings sort by lexicographical order
all_countries.sort()
print(all_countries)

# Numbers are sorted low to high
list_of_numbers = [60, 23.1, 0, 101, -10, -1.23, 5]
list_of_numbers.sort()
print(list_of_numbers)

## List with a mix of data types cannont be sorted automatically
# list_of_numbers = [60, 23.1, 0, "A", "B", "C"]
# list_of_numbers.sort()
# print(list_of_numbers)
## TypeError: '<' not supported between instances of 'str' and 'int'


print()
### Lenght of list
print(len(all_countries))


print()
### Iterating through a list
counter = 0
while counter < len(all_countries):
    print(all_countries[counter].upper())
    counter = counter + 1
