#Method Overloading
'''
post(image, song, caption, tag)
post(image, song, caption, tag)
'''
#Method overwriting
'''
p
post(img)
c
post(img)
'''

class Hotstar:
    def __init__(self, username):
        print(f"Hi {username} Welcome to the Hotstar".center(50, '-'))

    def playvideo(self):
        print("Movie with Ads")
        print("Limited access for movies")
        print("Quality is limited")
        print("One device login")
        print("No download option")
        print("No Live access")
        print("Sound Quality reduces")

    def login(self):
        print("Login is same")

    def interface(self):
        print("Same interface")

    def profile(self):
        print("Profile is same")


class PremiumUser(Hotstar):
    def __init__(self, username):
        print(f"Hi {username} Welcome to the Hotstar. Enjoy your premimum".center(50, '-'))

    # Method overriding (Polymorphism)
    def playvideo(self):
        print("Movie without Ads")
        print("Unlimited access for movies")
        print("High Quality")
        print("Multiple device login")
        print("Download option is available")
        print("Live access")
        print("Improved Sound Quality")


# Objects
satish = Hotstar("Satish")
satish.playvideo()
satish.login()

print()

randheer = PremiumUser("Randheer")
randheer.playvideo()
randheer.login()

#2.
class Instagram:
    def feed(self):
        print("Feed is same for all")

    def scrolling(self):
        print("Scrolling is same for all")

    def share(self):
        print("Share is same for all")

    def like(self):
        print("Like is same for all")

    def repost(self):
        print(  "Repost is same for all")

    def comment(self):
        print("Comment is same for all")

    def profile(self):
        print("No Professional dashboard")

    def posting(self):
        print("No insights are available")


class Creator(Instagram):
    # Overridden methods
    def profile(self):
        print("Professional dashboard is adding in their grid")

    def posting(self):
        print("You can see the reach, profile activites, followers")


krishna = Creator()
krishna.profile()
krishna.posting()

sanjeeva = Instagram()
sanjeeva.profile()
sanjeeva.posting()

#3. Operator Overloading
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num
    def __add__(self, other):
        return self.num + other.num
    
n1 = Number(10)
n2 = Number(20)

print(n1 + n2)
