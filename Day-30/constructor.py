
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

print(dheeraj.products)
print(dheeraj.name)

Flipkart.displaydiscount()
Flipkart.display()
print(Flipkart.products)

#using object ->ins, cls, sta , clsatt, insatt
#using class -> cls, sta , clsatt


#Constructor

class Flipkart:
    def __init__(self, name, phone):
            self.name=name
            self.phone=phone
            print(f"Hello {self.name}, Welcome to the flipkart")

dheeraj=Flipkart('dheeraj',9876543210)
rishi=Flipkart('rishi',9876540123)
sai=Flipkart('sai',9876501234)

    
#access private public protected attributes

class Instagram:
    def __init__(self, username, password):
        self.username=username
        self.__password=password
        self._posts=[]

    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self._posts

    def display(self):
        print(self.username,self.__password,self._posts)
        

dheeraj=Instagram('dheeraj','dheeraj@123')
dheeraj.display()
print(dheeraj.username)
print(dheeraj.getpassword())
print(dheeraj.accesspost)


#change username password posts

class Instagram:
    def __init__(self, username, password):
        self.username=username
        self.__password=password
        self._posts=[]

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password= newpassword

    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter
    def accessport(self,newpost):
        self._posts.append(newpost)

    def display(self):
        print(self.username,self.__password,self._posts)
        

dheeraj=Instagram('dheeraj','dheeraj@123')
dheeraj.display()
print(dheeraj.username)
print(dheeraj.getpassword())
print(dheeraj.accesspost)

dheeraj.username='sajid'
dheeraj.setpassword("sajid@123")
dheeraj.accesspost="sunrise.png"
dheeraj.accesspost="beach.png"
dheeraj.accesspost="forest.png"

print(dheeraj.username)
print(dheeraj.getpassword())
print(dheeraj.accesspost)












































































