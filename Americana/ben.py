name1 = input("Enter your first name:")
if name1 == "":
    print(name1,"name can not be emty")
else:
    print("Your name is", name1)
name2 = input("Enter your surname:")
if name2 == "":
   print(name2, "can not be emty")
else:
   print("Your name is",name1, name2)
   age = int(input("Enter your age:"))
   if age < 18:
    print("Your name is:",name1,name2,"Your age is:",age,"Your age is less than 18")
   if age > 18 and age <= 34:
    print("Your name is:",name1,name2, "Your age is:",age,"you are a youth")
   if age >= 35 and age < 100:
    print("Your name is:",name1,name2, "Your age is:",age,"you are an old citizen")

