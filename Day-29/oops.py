class Flipkart:
    products = {"shirts":1000,"handbag":2000,"pants":3000}
    discount=30


    @classmethod
    def display(cls):
        print(cls.products)

    def userinfo(self, name, phone, address):
        self.name=name
        self.phone=phone
        self.address=address
        print(f"Hello {self.name}, Welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% discount is going on, grab the products..")

dheeraj=Flipkart()
dheeraj.userinfo('dheeraj',9876543210,'Hyd')
dheeraj.displaydiscount()
dheeraj.display()

sai=Flipkart()
sai.userinfo('sai',9876543012,'che')
sai.displaydiscount()
sai.display()

rishi=Flipkart()
rishi.userinfo('rishi',9876540123,'ben')
rishi.displaydiscount()
rishi.display()