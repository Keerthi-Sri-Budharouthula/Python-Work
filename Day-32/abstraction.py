from abc import ABC,abstractmethod
class Phonepay(ABC):

    def senderinfo(self):
        print("You can enter their mobile number or scanner")
    def amount(self):
        print("You can enter amount")
    def pin(self):
        print("You need to enter the pin")

    @abstractmethod
    def transaction(self):
        pass

class HDFC(Phonepay):
    def transaction(self):
        print("Payment using hdfc bank")

class SBI(Phonepay):
    def transaction(self):
        print("Payment using sbi bank")

class UNION(Phonepay):
    def transaction(self):
        print("Payment using union bank")

class AXIS(Phonepay):
    def transaction(self):
        print("Payment using axis bank")

class ICIC(Phonepay):
    def transaction(self):
        print("Payment using icic bank")

vivek=HDFC()
vivek.senderinfo()
vivek.amount()
vivek.pin()
vivek.transaction()

sai=AXIS()
sai.senderinfo()
sai.amount()
sai.pin()
sai.transaction()

rishi=UNION()
rishi.senderinfo()
rishi.amount()
rishi.pin()
rishi.transaction()

sri=ICIC()
sri.senderinfo()
sri.amount()
sri.pin()
sri.transaction()

teja=SBI()
teja.senderinfo()
teja.amount()
teja.pin()
teja.transaction()


