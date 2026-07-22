def login(username, password):
    if username == "rasool" and password == "1627":
        print("Login successful!")
    elif username != "rasool" and password == "1627":
        print("Invalid username. Please try again.")
    elif username == "rasool" and password != "1627":
        print("Invalid password. Please try again.")
    else:
        print("Invalid username and password. Please try again.")   
username = input("Enter your username: ")
password = input("Enter your password: ")
login(username, password) 