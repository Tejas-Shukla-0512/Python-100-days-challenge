# 1
x=(1,4,9,16,25,36,49,64,81,100)
for i in x:
  print(i)

print("")

# 2
y = [1,4,9,16,25,36,49,64,81,100]
a= int(input("enter the no. :"))
ind=0
for j in y:
  print(j)
  if(j==a):
    print("found at",ind+1,"th position")
    break
  ind+=1

print("")

# 3
for k in range(2 ,10, 2): #matla start 1 se hoga end 10 pe hoga step 2 means 1 no chodh kar 
  print(k)

print("")

# 4
for l in range(100):
  print(l+1,end=" , ")

print("")
print("")

# 5
for m in range(101,1,-1):
  print(m-1,end=" , ")

print("")
print("")

# 6
for n in range(1,101):
  pass # matla kuch nhi karna hai 
