class Hotstar:
    def __init__(self,name):
        print(f"Welcome to the Hotstar, {name}")
    def login(self):
        print(f"You can login to the hotstar")
    def dashboard(self):
        print(f"You can see the dashboard")
    def search(self):
        print(f"You can search")
    def playcontrollers(self):
        print(f"pause.resume.play")
    def history(self):
        print(f"You can see the recent video")
    def ads(self):
        print("Ads will run")
    def quality(self):
        print("Quality is low")
    def access(self):
        print("You have only access for limited things")
    def download(self):
        print("You cannot download")
class Premium:
    def ads(self):
            print("Ads will not run")
    def quality(self):
            print("Quality is high")
    def access(self):
            print("You have unlimited access")
    def download(self):
            print("You can download with high quality")

a=Hotstar('sai')
a.download()
b=Premium()
b.download()