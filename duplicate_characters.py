def duplicate_char(string):
    list1 = list(string) # Converting the string to list of characters
    output = [i for i in list1 if list1.count(i) > 1]  # List comprehension to find the duplicate characters
    finall = list(set(output))   # Removing the duplicate characters
    return finall

# Dynamic data input from the user
string = input("Enter the string: ")
# Function call to find the duplicate characters in the string
response = duplicate_char(string)
print('Duplicate Characters',response)