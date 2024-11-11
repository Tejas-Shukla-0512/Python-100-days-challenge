a = int(input("enter your age:"))
print("your age is:",a)

# some conditional operators
# >, <, >=, <=, ==, !=

if(a>=18):
  print("you can vote")
else:
  print("you cannot vote")
print("")

price = int(input("enter the price:"))
budget = int(input("enter your budget:"))
if (budget - price >= 50):
  print("you can buy")
elif (budget - price >= 30):
  print("it's ok-ok you can buy it")
else:
  print("you cannot buy")
print("")

num = int(input("Enter the Number"))
if (num > 0):
  print("Number is positive")
elif(num == 0):
  print("Number is zero")
else:
  print("Number is negative")
print("")

num2 = int(input("Enter the Number"))
if (num2 < 0):
  print(num2, "is negative")
elif(num2 > 0):
  print(num2, "is positive")
  if(num2<=10):
    print(num2, "is between 1-10")
  elif(num2 <= 20):
    print(num2, "is between 11-20")
  else:
    print(num2,"is greater than 20")
