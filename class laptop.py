class laptop:
    def __init__(self,brand,ram):
        self.brand=brand
        self.ram=ram
    def showlaptop(self):
        print(f"{self.brand}:{self.ram}")
s1=laptop("lenovo",16)
s2=laptop("asus",18)
s1.showlaptop()
s2.showlaptop()
                       
