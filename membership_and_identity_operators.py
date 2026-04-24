#membership operator
l = [1, 2, 3, 4, 5]
s = "Hello World"
d = {1: "Nistha", 2: "Is", 3: "Devi"}

print(5 in l)
print('O' in s)
print(4 in d)

# identity operator 
n1 = 10
n2 = 10
b = [1,2,3]
c = [2,3,4]
a = c

s1 = "Hello"
s2 = "hello"


print(n1 is n2) #returns True
print(a is c) #returns True
print(b is c) #returns False
print(s1 is s2) #returns False


