names = "tejas,kushi"
# to find the length of a string use len() function
print(len(names))
print("")
# if we want to print a particular characters of a string then we use []
a = "tejas"
# point that the first character of a string is always 0
# last 4 will not be printed it prints till 3
# it is because we need 4 cahracters to print not till 4
print(len(a))
print(a[0:4])
print(a[1:4])
# it will auto add 0 at the starting
print(a[:3])
# it will print till the last character
print(a[:])
print("")
# negative slicing
print(a[-3:-1])
# first it will convert the negative index into positive index
# total no. in 5 ane we give -3 so, 5-3=2 then it starts with 2 and 5-1=4 so it will print till 4
print(a[-4:-1])
# 5-4=1 and 5-1=4 so it will print from 1 to 4
print(a[-5:])
nm = "harry"
print(nm[-4:-2])
