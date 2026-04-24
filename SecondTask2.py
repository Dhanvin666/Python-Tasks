#>>Create a program for creating bank accound in which ask details 
#to add them in a dictionary(name as key and other details in a dictionary )

#>>And after that ask user that how much money he wants to cashback then subtract 
#that amount from the balance of user and print the final details of user.

#>>create a blank dictionary named as users = {}

#>>then create some variables to ask user information like: name = input("Enter Name:")
#ask name, lastname, age, adharcardno, profession, openingBalance, PANcardNo, Address

#>>and then add all these data into the users dictionary as 
#users[name] = {"name":name, "lastname":lastname,  like this add others}


#>>and then in last print("Account created successfully)
#print(users[name]) 👈we are printing users[name] 
#>>because account create karne pe sirf uski details print karwani h naki pure bank ki


Name = input("Enter Name:")
Lastname = input("Enter Lastname:")
Age = input("Enter Age:")
Adharcard_No = input("Enter Adharcard_No:")
Profession = input("Enter Profession:")
Opening_Balance = input("Enter Opening_Balance:")
PANcard_No = input("Enter PANcard_No:")
Address = input("Enter Address:")

sbi = {}

sbi[name] = {"Name":Name,"Lastname":Lastname,"Age":Age,"Adharcard_No":Adharcard_No,"P"}