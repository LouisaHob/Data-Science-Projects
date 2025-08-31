"""
Program that reads from the text file 'DOB.txt' and separates names and birth dates into two lists.
Read the contents of the file, and return them a list of strings (name and birth date).
Create lists to store names and birth dates in the variables 'names' and 'birth_date'.
The program then iterates through each line using a for loop.
The program then checks through each character in the length of the line to find the first digit (is.digit()).
Once the program finds the first digit, it splits the line at that point.
Everything before the digit is stored in the variable 'name', and everything after the digit is stored in the variable 'birth_date'.
The 'name' is then appended to the 'names' list, and the 'birth_date' is appended to the 'birth_dates' list.
Break when the first digit is found and the line is split.
The program will then print the names and birth dates on separate lines in two separate lists.
"""

# Read the contents of the DOB.txt file
with open('DOB.txt', 'r') as file:
    lines = file.readlines()

#Create lists to store names and birth dates
names = []
birth_dates = []

# Process each line to separate names and birth dates based on the first digit
for line in lines:
    for i in range(len(line)):
        if line[i].isdigit():
            # Split the line at the first digit: before is the name, after is the birth date
            name = line[:i].strip()
            birth_date = line[i:].strip()

            # Append to the lists
            names.append(name)
            birth_dates.append(birth_date)
            break

# Print names and birth dates in the required format
print("Name:")
for name in names:
    print(name)  # Print each name on a new line

print("\nBirthdate:")
for birth_date in birth_dates:
    print(birth_date)  

#Voila!
