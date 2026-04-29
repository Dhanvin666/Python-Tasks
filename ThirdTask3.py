user_details = {}

while True:

    print("1 For Creating Account,  \n2 For Deleting Account, \n3 For Add Money, \n4 For  Withdraw Money, \n5 For Sending Money To Receiver")
    choice = input("Enter Choosen Number: ")

    if choice == "1":
        first_name = input("Enter First_Name: ")
        last_name = input("Enter Last_Name: ")
        mobile_no = int(input("Enter Mobile_No.: "))
        age = int(input("Enter Age: "))
        opening_bal = int(input("Enter Opening_Balance: "))

        user_details[first_name] = {"first_name":first_name, "last_name":last_name, "mobile_no.":mobile_no,
                                    "age":age, "opening_bal":opening_bal}

        print("\n\n\n Account Created Successfully")
        print(f"Account Details: \nfirst_name:{first_name} \nlast_name:{last_name} \nmobile_no:{mobile_no} \nage:{age} \nopening_bal:{opening_bal}")

    if choice == "2":
        delete_first_name = input("Enter your name to delete the account: ")
        del user_details[delete_first_name]
        print("your account has been deleted")

        print(user_details)

    if choice == "3":
        nametoaddmoney = input("Enter name as per given while creating account: ")

        amount = int(input("Enter amount you want to add: "))
        user_details[nametoaddmoney]["opening_bal"] = user_details[nametoaddmoney]["opening_bal"] + amount
        d = {user_details[nametoaddmoney]["opening_bal"]}
        print(f"Your account has been credited with {amount} and final balance is {d}")

    if choice == "4":
        nametowithdrawmoney = input("Enter name as per given while creating account: ")

        amount = int(input("Enter amount you want to Withdraw: "))
        user_details[nametowithdrawmoney]["opening_bal"] = user_details[nametowithdrawmoney]["opening_bal"] - amount

        
        print(f"Your account has been Withdraw with {amount} and final balance is {user_details[nametowithdrawmoney]['opening_bal']}")


    if choice == "5":

        nameofsender = input("Enter name of sender as per given while creaing account: ")
        amount = int(input("Enter amount you want to send: "))
        nameofreceiver = input("Enter name of receiver as per given while creting account: ")

        user_details[nameofsender]["opening_bal"] = user_details[nameofsender]["opening_bal"] - amount
        user_details[nameofreceiver]["opening_bal"] = user_details[nameofreceiver]["opening_bal"] + amount

        print(f"{nameofsender} send this {amount} to {nameofreceiver} and final balance of {nameofsender} is {user_details[nameofsender]['opening_bal']}")

        # print(f"You recived this {amount} and final balance is {user_details[nameofreceiver]['opening_bal']}")


        