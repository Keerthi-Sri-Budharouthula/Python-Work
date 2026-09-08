#super method is used to extract features from parent class having same method name different features
#it is always pointing to single parent
class whatsappv1:
    def status(self):
        print("You can add images and videos")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("You can add music and stickers")

class whatsappv3(whatsappv2):
    def status(self):
        super().status()
        print("You can like and you can add reaction")


a=whatsappv3()
a.status()




