tasklist = {}

while True:
    print("1. Add, \n2. Remove, \n3. Print, \n4. Enter Update Task")
    choise =  input("Enter Choosen Number: ")

    if choise == "1":
        taskname = input("Enter taskname: ")
        deadline_in_days = input("Enter deadline_in_days: ")
        description = input("Enter description: ")
        status = input("Enter status: ")

        tasklist[taskname] = {"taskname":taskname, "deadline_in_days":deadline_in_days, "description":description,"status":status}

        print("\n\n\n List Added Successfully")
        print(f"Tasklist Details \ntasknumber:{taskname} \ndeadline_in_days:{deadline_in_days} \ndescription:{description} \nstatus:{status}")

    if choise == "2":
        delete_taskname = input("Enter your taskname to delete your account: ")
        del tasklist[delete_taskname]
        print("Your tasklist details has been deleted")

        print(tasklist)
    
    if choise == "3":
        print("\n Total Tasklist: ")
        print()

# retyuytryut
