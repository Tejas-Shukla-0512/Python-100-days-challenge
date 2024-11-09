# Input tag 
# it allow user to input any value
a = input()
print("you input:",a)
# input always take string value by default
b = input("your input:")
print(type(b),b)
# we can change the type of input value by typecasting
# hear your c is int but d float so python change c to float autometically
c = int(input("your input:"))
d = float(input("your input:"))
print(c+d)
print(type(c),type(d))
# another way is 
x = input("type:")
y = input("type:")
print(int(x)+int(y))
