'''
single a->b
mutliple a,b,c,d->e
multi level a->b->c
heirarchal a->b,c,d,e
hybrid  + combination of any two inheritances 
'''

#single inheritance

class whatsappV1:
    def __init__(self,name):
        self.name = name
        print(f"Welcome to the whatsapp - v1 {self.name}!")
    def messaging(self):
        print("You can send messages")

class whatsappV2(whatsappV1):
    def __init__(self,name):
        self.name = name
        print(f"Welcome to the whatsapp - v2 {self.name}!")
    def calls(self):
        print("You can audio and video calls")

rishi=whatsappV1('rishi')
rishi.messaging()

sai=whatsappV2('sai')
sai.messaging()
sai.calls()


























































































