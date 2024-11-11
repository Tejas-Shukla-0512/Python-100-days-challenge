import time
name = input("What is your name? ")
a = name.upper()
time = time.strftime('%H:%M:%S')
if(time >= "04:00:00"and time <= "12:59:59"):
  print("hey",a ,"good morning")
  print("it's",time)
elif(time >= "12:00:00"and time <= "16:59:59"):
  print("hey",a ,"good afternoon")
  print("it's",time)
elif(time >= "17:00:00"and time <= "20:59:59"):
  print("hey",a ,"good evening")
  print("it's",time)
else:
  print("hey",a ,"good night")
  print("it's",time)




# Morning Time : 04:00:00 to 11:59:59
# Afternoon Time : 12:00:00 to 16:59:59
# Evening Time : 17:00:00 to 20:59:59
# Night Time : 21:00:00 to 03:59:59

