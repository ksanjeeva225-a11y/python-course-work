#Attributes
'''
1. Instance - object name
2. Class - obect name, class name
'''

#Methods
'''
1. class - objname, clsname - cls @class method
2. instance - objname - self
3. static - object name, class name -''- @static method
'''

class Instagram:
    settings = ['Ins', 'Sta', 'Pri']

    @classmethod
    def settingsupdate(cls):
        print(cls.settings)

    @staticmethod
    def welcome():
        print("Welcome to Instagram. Have Fun!!")

    def userdetails(self, username, password, bio=''):
        self.username = username
        self.password = password
        self.bio = bio

        print(f"Hello {self.username}\nWelcome to Instagram. Have Fun!!")
        

# Create an instance of Instagram
randheer = Instagram()
randheer.userdetails("Randheer", "r@123")

# Print instance-specific details
print(randheer.username)  # Randheer
print(randheer.password)  # r@123
print(randheer.bio)  # ''
print(Instagram.settings)  # ['Ins', 'Sta', 'Pri']

# Call class method and static method via the instance
randheer.settingsupdate()  # Prints the settings
randheer.welcome()  # Prints the welcome message

# Create another instance of Instagram
harsha = Instagram()
harsha.userdetails("Harsha", "H@123", "My Life My Rule")

# Print harsha's user details
print(harsha.username)  # Harsha
print(harsha.password)  # H@123
print(harsha.bio)  # My Life My Rule


#2. With constructors
class Instagram:
    settings = ['Ins', 'Sta', 'Pri']

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bio = ''
        self.followers = []
        self.following = []
        print("Welcome to Instagram. Have Fun!!")
        print(f"Username : {self.username}")
        print(f"Password : {self.password}")
    

randheer = Instagram("Randheer", "r@123")

#3. With access modifiers
class Instagram:
    settings = ['Ins', 'Sta', 'Pri']

    def __init__(self, username, password):
        print("Welcome to Instagram. Have Fun!!")
        
        # Public variable (can be accessed & modified outside)
        self.username = username
        
        # Private variable (cannot be accessed directly)
        self.__password = password
        
        # Protected variable (used internally / subclasses)
        self._post = []

    # Getter method to read private password
    def getPassword(self):
        return self.__password

    # Setter method to update private password
    def setPassword(self, newPassword):
        self.__password = newPassword
        print("Password Updated")

    @property
    def viewPost(self):
        return self._post

    @viewPost.setter
    def viewPost(self, post):
        self._post.append(post)

randheer = Instagram("Randheer", "r@123")
print(f"Before Username: {randheer.username}")
randheer.username = "Sumanth"
print(f"After Username: {randheer.username}")

print(f"Before Password: {randheer.getPassword()}")
randheer.setPassword("Sumanth@123")
print(f"After Password: {randheer.getPassword()}")

print(randheer.viewPost)
randheer.viewPost = "hello"
randheer.viewPost = "First Reel"
print(randheer.viewPost)
