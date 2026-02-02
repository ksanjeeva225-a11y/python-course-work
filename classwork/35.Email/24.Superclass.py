#1. Super Method
class Whatsapp_v1:
    def status(self):
        print("Upload picture and video with limited duration")

class Whatsapp_v2(Whatsapp_v1):
    def status(self):
        super().status()
        print("You can like the status and mention your friends")

krishna = Whatsapp_v2()
krishna.status()

#1. Super Method
class Whatsapp_v1:
    def status(self):
        print("Upload picture and video with limited duration")

class Whatsapp_v2:
    def status(self):
        print("You can like the status and mention your friends")

class Whatsapp_v3(Whatsapp_v1, Whatsapp_v2):
    def status(self):
        Whatsapp_v1.status(self)
        Whatsapp_v2.status(self)
        print("You can share music and share it on cross platform as as well")
        
krishna = Whatsapp_v3()
krishna.status()
