# any think in "", '' are conciderd as string
# print("hello world") hello word is string 
print("hello world")
print("")
# if ve have to add symbols like('',"") we have to use \ before the symbol
print("hello world \"i am a good boy\"")
# to print mulitple line we have to use \n or we can use ''' '''
print("")
print("hello world \nhello tejas and everyone")
# we can use any symbol in ''' ''' string
a = '''hello world          
hello tejas and "everyone"
this is a 'multiline string'''
print(a)

# we string is 0,1,2,3,4
#              T,e,j,a,s
# so if we want to print any latter from string we have to use []
b = "Tejas"
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
# if we add 5 the it gives an eorror print(a[5])
print("")
# we can also use for loop to print all latter in string
for character in a:
  print(character)
