
# Vertical text
word = "The quick brown fox"
i = 0
while i < len(word):
    print(word[i])
    i += 1
print()
print()


# Guest list
guest_list = ""
while True:
    inpt = input("Who would you like to invite?")
    if inpt == "done":
        break
    else:
        guest_list += inpt + ", "
print("Dear", guest_list, "\n\tYou're invited!")
