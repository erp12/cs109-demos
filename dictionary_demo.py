# create dict

state_capitals = {}


# Set elements of dict

state_capitals["MA"] = "Boston"
state_capitals["NY"] = "Albany"
state_capitals["CA"] = "Sacramento"
print(state_capitals)


# Get number of key-value pairs in dict
print(len(state_capitals))


# Get value from from dict using key
ny_capital = state_capitals["NY"]
print(ny_capital)


# Can overwrite key-value pairs
state_capitals["MA"] = "Amherst"

print()

# keys() method
states = state_capitals.keys()
print(states)


# values() method
capitals = state_capitals.values()
print(capitals)

print()

# Iterating over dict
for k, v in state_capitals.items():
    print("The capital of " + k + " is " + v)

print()

# A common method for storing data
state_data = [
    {
        "name" : "California",
        "abbr" : "CA",
        "capital" : "Sacremento",
        "population" : 39250000,
    }, {
        "name" : "Alabama",
        "abbr" : "AL",
        "capital" : "Montgomery",
        "population" : 4863000,
        
    }, {
        "name" : "Massachusetts",
        "abbr" : "MA",
        "capital" : "Boston",
        "population" : 6812000
    }, {
        "name" : "New Jersey",
        "abbr" : "NJ",
        "capital" : "Trenton",
        "population" : 8944000
    }, {
        "name" : "New York",
        "abbr" : "NY",
        "capital" : "Albany",
        "population" : 19750000
    }
]


biggest_population = 0
biggest_state = None

for state in state_data:
    if state["population"] > biggest_population:
        biggest_state = state
        biggest_population = state["population"]
    
print("The biggest state is " + biggest_state["name"])
print("and the capital is " + biggest_state["capital"])
