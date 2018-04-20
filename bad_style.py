from operator import add


list_of_numbers = []

for i in range(10):
    
    if len(list_of_numbers) < 2:
        newNumber = 1
    else:
        newNumber=add(list_of_numbers[-2], list_of_numbers[-1])
        
    list_of_numbers.append(newNumber)
    print(newNumber)
