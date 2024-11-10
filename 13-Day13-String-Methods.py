a = "Tejas shukla"
# to print the length of the string
print(len(a))
print("")
# to print the string in upper case
print(a.upper())
print("")
# to print the string in lower case
print(a.lower())
print("")
# to remove symbols or last words from the string
print("")
b = "teajs**#$%"
print(b.rstrip("*%#$"))
c = "tejas shukla"
print(a.rstrip("shukla"))
print("")
# to replace the string
print(c.replace("tejas","harry"))
print("")
# to split the string
d = "tejas shakshi tejaswini"
print(d.split(" "))
print("")
# to capitalize the first letter of the string
# it also correct the error in the sentence
e = "tEjas shUklA"
print(e.capitalize())
print("")
# to center the string
print(len(a))
print(len(a.center(50)))
print(a.center(50))
print("")
# to count the number of times a word has occured in the string
f = "tejas shakshi khushi tejas"
print(f.count("tejas"))
print("")
# to check the string ends with the given word
print(f.endswith("tejas"))
print(f.endswith("shakshi",4,13))
print("")
# to find the index of the given word
print(f.find("shakshi"))
# if index did not fount the it gives error
# print(f.index("tejassd"))
print("")
# to check the string is alpha numeric or not A-Z,a-z,0-9
g = "tejasisagoodboy"
h = "tejas is a good boy"
i = "12342"
j = "Tejasshukal0512"
print(g.isalnum())
print(h.isalnum())
print(i.isalnum())
print(j.isalnum())
print("")
# to check the string is in lower/upper case or not
k = g
print(g.islower())
l = "TEJAS"
print(l.isupper())
print("")
# to check the string is printable or not
m = "tejas is a good boy\n"
print(m.isprintable())
print("")
# to check the string contains space or not
print(m.isspace())
n = "  "
print(n.isspace())
print("")
# to swap the case of the string
o = "Tejas Shukla"
print(o.swapcase())
print("")
# to conver the string in title case
p = "he's is a good boy his name is tejas"
print(p.title())

