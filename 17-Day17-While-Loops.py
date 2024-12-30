# # 1
# a = 1
# while a<=100:
#   print(a,end=" , ")  
#   a+=1

# print("");print("")

# # 2
# b = 100
# while b>=1:
#   print(b,end=" , ")
#   b-=1

# print("");print("")

# # 3
# i = int(input("Enter the number: "))
# c = 1
# while c<=10:
#   print(i,"x",c,"=",i*c)
#   c+=1

# print("");print("")


# # 4

# ls=[1,4,9,16,25,36,49,64,81,100]
# d = 0
# while d<len(ls):
#   print(ls[d],end=" , ")
#   d+=1

# print("");print("")

# # 5

nums =(1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the number: "))
i = 0
while i<len(nums):
  
  if nums[i] == x:
    print(x , "is founded", "at index",i+1)  
    break
  else:
    print("finding....")

  i+=1
  
