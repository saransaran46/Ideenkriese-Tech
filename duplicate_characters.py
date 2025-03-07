def duplicate_char(string):
    list1 = list(string)
    output = [i for i in list1 if list1.count(i) > 1]
    finall = list(set(output))
    return finall
    
string = input("Enter the string: ")
response = duplicate_char(string)
print('Duplicate Characters',response)