class car:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour= colour
    def show(self):
        print("brand:",self.brand)
        print("colour:",self.colour)
s1=car("tata sierra","luna grey")
s1.show()