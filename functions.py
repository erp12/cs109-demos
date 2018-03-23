
def print_max(a, b):
   if(a > b):
      print(str(a) + " is greater than " + str(b))
   elif(b > a):
      print(str(b) + " is greater than " + str(a))

print_max(6, 11)
print(max(6, 11))


# First and Last character
def first_and_last(s):
    return s[0] + s[-1]

print(first_and_last("Hello"))
print(first_and_last("Goodbye"))


# Every other digit
def every_other_digit(num):
    num_as_str = str(num)
    digits = ""
    i = 0
    while i < len(num_as_str):
        if i % 2 == 0:
            digits = digits + num_as_str[i]
        i += 1
    return int(digits)

print(every_other_digit(54123))
print(every_other_digit(15151515))
