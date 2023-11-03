import time
name= input("Enter your name: ")
print(name)
Gender= input("Type your gender:")
input("Press Enter To Continue")
Hour = int(time.strftime('%H'))
Minute = int(time.strftime('%M'))
Second= int(time.strftime('%S'))
print(Hour,":",Minute,":",Second)
if(Gender=="Male"):
   
 if (Hour>5 and Hour<12):
  print("good morning",name, "sir")
 elif(Hour>=12 and Hour<=18):
  print("good afternoon",name, "sir")
 elif(Hour>18 and Hour<22):
  print("Good Evening," ,name, "sir")
 else:
  print("good night", name,"sir")

else:
 
 if (Hour>5 and Hour<12):
  print("good morning",name, "ma'am")
 elif(Hour>=12 and Hour<=18):
  print("good afternoon",name, "ma'am")
 elif(Hour>18 and Hour<22):
  print("Good Evening," ,name, "ma'am")
 else:
  print("good night", name,"ma'am")