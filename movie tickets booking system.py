class movieticket:
    def __init__(self,name,id,price):
        self.moviename = name
        self.movieid = id
        self.ticketprice = price
    def booktickets(self):
        self.moviename = input("enter name of movie :")
        total = input("enter no.of tickets")
        amount = total*self.ticketprice
    def display(self):
        print(f"")