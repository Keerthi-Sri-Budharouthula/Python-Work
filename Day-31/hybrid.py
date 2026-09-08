class whatsappv1:
    def messaging(self):
        print("You can messages")

class whatsappv2:
    def extramessage(self):
        print("You can add emojis, stickers and gifs")

class whatsappv3(whatsappv1,whatsappv2):
    def  calls(self):
        print("You can audio and video calls")

class whatsappv4(whatsappv3):
    def status(self):
        print("You can add the status for 24 hours")
    
    

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.extramessage()

c=whatsappv3()
c.messaging()
c.extramessage()
c.calls()

d=whatsappv4()
d.messaging()
d.extramessage()
d.calls()
d.status()