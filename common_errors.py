### Error
### ZeroDivisionError: division by zero

##denominator = 0
##numerator = 5
##numerator / denominator

### FIX

##denominator = 1
##numerator = 5
##numerator / denominator



### Error
### NameError: name 'x' is not defined

##y = x + 5
##x = 1001
##print(y)

### FIX

##x = 1001
##y = x + 5
##print(y)




### Error
### NameError: name 'my_Dogs_name' is not defined

##my_dogs_name = "Spot"
##print(my_Dogs_name)

### FIX

##my_dogs_name = "spot"
##print(my_dogs_name)



### Error
### SyntaxError: expected indent block

##animal_type = "reptile"
##if animal_type == "mammal":
##print("Often fluffy.") 
##else:
##print("Not fluffy.")

### FIX

##animal_type = "reptile"
##if animal_type == "mammal":
##    print("Often fluffy.") 
##else:
##    print("Not fluffy.")



### Error
### SyntaxError: unexpected indent

##f_name = "Han"
##l_name = "Solo"
##    full_name = f_name + " " + l_name
##print(full_name)

### Fix

##f_name = "Han"
##l_name = "Solo"
##full_name = f_name + " " + l_name
##print(full_name)



### Error
### SyntaxError: invalid syntax

##animal_type = "reptile"
##if animal_type = "mammal":
##    print("Often fluffy.") 
##else:
##    print("Not fluffy.")

### FIX

##animal_type = "reptile"
##if animal_type == "mammal":
##    print("Often fluffy.") 
##else:
##    print("Not fluffy.")



### Error
### IndexError: string index out of range

##school_name = 'Hampshire College'
##c = school_name[45]
##print(c)

### FIX

##school_name = 'Hampshire College'
##c = school_name[4]
##print(c)
