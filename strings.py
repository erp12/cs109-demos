my_string = "Hello Hampshire!"


### Computing string length
print("String length:", len(my_string))
print()


# Indexing single characters
ndx = 1
print("Char at ndx:", my_string[ndx])
print()


# Concatenation of multiple strings
my_name = "Elmo"
greeting = "Hello " + my_name + ". How are you?"
print(greeting)
print()


# Repeating strings
print(greeting * 3) # greeting + greeting + greeting
print()

print((greeting + "\n") * 3)


# slicing strings
print(my_string[1:5])
my_string_tail = my_string[6:-1]
print(my_string_tail)
print(len(my_string_tail))
print()


# Put it all together
tv_show_name = (my_name + "'s ") + my_string[6:]
print(tv_show_name)
