#punctuations  =  {} , ? <,>,: ,"",@,# ^, % ! ,(), *,- , = 
#  if for a string , we will do iteration for each letter of the string using a for loop 


punc  = '''!{}()=-[];:'"<>?@$%^&*~'''
string = input ("Enter anything : ")

for char in string:
    if char in punc:
        string = string.replace(char, "")

print(string)       


# or 
empty_str = ""
for i in string :
    if i not in punc :
        empty_str += i
        
print (empty_str)
