d={"lilly": "7793923748", "umesh": "8688012605", "muzeeb": "9876543210", "rahul": "9123456789", "raghava": "9988776655"}
print("ADD CONTACT[1]")
print(" SEARCH CONTACT[2]")
print(" UPDATE CONTACT[3]")
print(" DELETE CONTACT[4]")
print(" DISPLAY ALL CONTACT[5]")
print("   ")
option=int(input("enter the option:"))
if option==1:
    name=input("enter the name:")
    number=input("enter the number")
    d[name]=number
    print("contact added successfully")
    print(d)
elif option==2:
    name=input("enter the name:")
    if name in d:
        print("contact found")
        print(d[name])
    else:
        print("contact not found")
        print(d)
elif option==3:       
    name=input("enter the name")
    if name in d:
        print("contact found")
        number=input("enter the new number")
        d[name]=number
        print("contact updated successfully")
        print(d)
    else:
        print("contact not found")
        print(d)
elif option==4:
    name=input("enter the name:")
    if name in d:
        print("contact found")
        del d[name]
        print("contact deleted successfully")
        print(d)
    else:
        print("contact not found")
        print(d)
else:
    print("displaying all contacts")
    print(d)