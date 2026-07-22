file=open("trail.txt","a")
file.write("\nmy friends")
file.close()

file=open("trail.txt","r")
print(file.readlines())
file.close()