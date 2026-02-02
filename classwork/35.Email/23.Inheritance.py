#Inheritance
'''
1. single Inheritance - a -> b
2. multiple Inheritance - a, b, c -> d
3. multilevel Inheritance - a -> b -> c -> d
4. hierarchical Inheritance - a ->b, c, d
5. hybrid Inheritance
'''
#1. Single Inheritance
class Whatsapp_v1:
    def messaging(self):
        print("You can message")

    def sharepics(self):
        print("You can share the photos")

class Whatsapp_v2(Whatsapp_v1):
    def status(self):
        print("You can upload the status")
    def videos(self):
        print("You can send videos also")

imran = Whatsapp_v1()
print("Imran - v1")
imran.messaging()
imran.sharepics()

santosh = Whatsapp_v2()
print("Santosh - v2")
santosh.messaging()
santosh.sharepics()
santosh.status()
santosh.videos()

#2. Multilevel Inheritance
class Whatsapp_v1:
    def messaging(self):
        print("You can message")

    def sharepics(self):
        print("You can share the photos")

class Whatsapp_v2(Whatsapp_v1):
    def status(self):
        print("You can upload the status")
    def videos(self):
        print("You can send videos also")

class Whatsapp_v3(Whatsapp_v2):
    def calls(self):
        print("You can do video or audio calls")
    def groups(self):
        print("You can create groups in this version.")

imran = Whatsapp_v1()
print("\nImran - v1")
imran.messaging()
imran.sharepics()

santosh = Whatsapp_v2()
print("\nSantosh - v2")
santosh.messaging()
santosh.sharepics()
santosh.status()
santosh.videos()

harsha = Whatsapp_v3()
print("\nHarsha - v3")
harsha.calls()
harsha.groups()
harsha.messaging()
harsha.sharepics()
harsha.status()
harsha.videos()

#3. Multiple Inheritance
class Whatsapp_v1:
    def messaging(self):
        print("You can message")

    def sharepics(self):
        print("You can share the photos")

class Whatsapp_v2(Whatsapp_v1):
    def status(self):
        print("You can upload the status")
    def videos(self):
        print("You can send videos also")

class Whatsapp_v3(Whatsapp_v2):
    def calls(self):
        print("You can do video or audio calls")
    def groups(self):
        print("You can create groups in this version.")

class Community:
    def clubgroup(self):
        print("You can create a community with clubing the groups.")

class Meta:
    def ai(self):
        print("You can chat, generate images, generate videos")

class Whatsapp_v4(Whatsapp_v3, Community, Meta):
    def channel(self):
        print("You can create channel to engage with your followers.")

imran = Whatsapp_v1()
print("\nImran - v1")
imran.messaging()
imran.sharepics()

santosh = Whatsapp_v2()
print("\nSantosh - v2")
santosh.messaging()
santosh.sharepics()
santosh.status()
santosh.videos()

harsha = Whatsapp_v3()
print("\nHarsha - v3")
harsha.calls()
harsha.groups()
harsha.messaging()
harsha.sharepics()
harsha.status()
harsha.videos()

randheer = Whatsapp_v4()
print("\nRandheer - v4")
randheer.calls()
randheer.groups()
randheer.messaging()
randheer.sharepics()
randheer.status()
randheer.videos()
randheer.channel()
randheer.clubgroup()
randheer.ai()

#4. hierarchical Inheritance
class Whatsapp_v1:
    def messaging(self):
        print("You can message")

    def sharepics(self):
        print("You can share the photos")

class Whatsapp_v2(Whatsapp_v1):
    def status(self):
        print("You can upload the status")
    def videos(self):
        print("You can send videos also")

class Whatsapp_v3(Whatsapp_v2):
    def calls(self):
        print("You can do video or audio calls")
    def groups(self):
        print("You can create groups in this version.")

class Community:
    def clubgroup(self):
        print("You can create a community with clubing the groups.")

class Meta:
    def chat(self):
        print("You can chat")

class Meta1(Meta):
    def ai_images(self):
        print("You can genetate images")

class Meta2(Meta):
    def human_emotions(self):
        print("You can share your feelings")

class Meta3(Meta1, Meta2):
    def technical(self):
        print("You can ask technical question also, Meta can provide all kind of things")

class Whatsapp_v4(Whatsapp_v3, Community, Meta3):
    def channel(self):
        print("You can create channel to engage with your followers.")

imran = Whatsapp_v1()
print("\nImran - v1")
imran.messaging()
imran.sharepics()

santosh = Whatsapp_v2()
print("\nSantosh - v2")
santosh.messaging()
santosh.sharepics()
santosh.status()
santosh.videos()

harsha = Whatsapp_v3()
print("\nHarsha - v3")
harsha.calls()
harsha.groups()
harsha.messaging()
harsha.sharepics()
harsha.status()
harsha.videos()

randheer = Whatsapp_v4()
print("\nRandheer - v4")
randheer.calls()
randheer.groups()
randheer.messaging()
randheer.sharepics()
randheer.status()
randheer.videos()
randheer.channel()
randheer.clubgroup()
randheer.chat()
randheer.ai_images()
randheer.technical()
randheer.human_emotions()
