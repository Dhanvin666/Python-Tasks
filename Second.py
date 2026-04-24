#Write a program to ask user about insta_account creation.

name = input("Enter Name:")
age = input("Enter Age:")
gender = input("Enter Gender:")
Email = input("Enter Email:")
mobile_no = input("Enter Mobile_No.:")

hobbylist = []
n = int(input("Number of Hobby:"))

for i in range(n):
    hobby = input("Enter Hobby:")
    hobbylist.append(hobby)

password = input("Enter Password:")
Re_password = input("Enter Re_Password:")

accountuser = {}

accountuser[name] = {"name":name,"age":age,"gender":gender,"email":Email,"mobile_no":mobile_no,
                    "hobby":[hobbylist],"password":password,"Re_password":Re_password}
            
print(accountuser)