#multiple inheritance->single child multiple parents
class whatsappv1:
    def messaging(self):
        print("You can send messages")

class whatsappv2:
    def calls(self):
        print("You can audio and video calls")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        print("You can add the status for 24 hours")

a=whatsappv1()
a.messaging()

b=whatsappv2()
#b.messaging()
b.calls()

c=whatsappv3()
c.messaging()
c.calls()
c.status()



class whatsappv1:
    def status(self):
        print("You can add images and videos")

class whatsappv2:
    def status(self):
        print("You can add music and stickers")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("You can like and you can add reaction")


a=whatsappv3()
a.status()










































































































































































