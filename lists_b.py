# First N numbers of the fibonacci sequence

n = 10
fib_numbers = []

i = 0
while i < n:
    if len(fib_numbers) < 2:
        fib_numbers.append(1)
    else:
        next_fib_number = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_fib_number)
    i += 1
print(fib_numbers)




# Contact list

my_contact_list = ["Mark=1-989-384-8933", "Serena=404-576-2542"]

looping = True
while looping:
    new_contact_name = input("Enter a name: ")
    new_contact_phone = input("Enter " + new_contact_name + "'s number: ")
    new_contact = new_contact_name + "=" + new_contact_phone 
    my_contact_list.append(new_contact)

    looping = input("Add another? y/n ") == 'y'
my_contact_list.sort()
print(my_contact_list)
