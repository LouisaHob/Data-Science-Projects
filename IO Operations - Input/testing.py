name_birth = "Orville Wright 21 July 1988"
name = ""
birth = ""

for i in name_birth:
    if i.isdigit():
        birth += name_birth[name_birth.index(i):] + "\n" # Slices the string starting from the index returned by name_birth.index(i) and adds a newline character
        break
    else:
        name += i

print("Name")
print(name)

print("\n")          # Need to figure out how to add a \n to the end of the name

print("Birthdate")
print(birth)



