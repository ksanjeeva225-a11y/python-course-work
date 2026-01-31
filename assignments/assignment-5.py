from abc import ABC, abstractmethod

# ------------------------------------------------------------
# ABSTRACTION
# ------------------------------------------------------------

class User(ABC):

    total_users = 0

    def __init__(self, name, email, password):
        self.name = name
        self._email = email              
        self.__password = password       
        User.total_users += 1

    def login(self, password):
        return self.__password == password

    @abstractmethod
    def display_info(self):
        pass


# -----------------------------------------------------------
# INHERITANCE
# ------------------------------------------------------------

class Learner(User):

    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.enrolled_courses = {}       
        self.certificates = []

    def enroll_course(self, course):
        self.enrolled_courses[course.title] = 0
        CourseraPlatform.total_revenue += course.price
        print(f"{self.name} enrolled in {course.title}")

    def update_progress(self, course_title, progress):
        if course_title in self.enrolled_courses:
            self.enrolled_courses[course_title] = progress
            if progress == 100:
                cert = Certificate(self.name, course_title)
                self.certificates.append(cert)
                cert.generate()

    # POLYMORPHISM
    # --------------------------------------------------------
    def display_info(self):
        print(f"👨‍🎓 Learner: {self.name}")
        print("Courses Enrolled:", list(self.enrolled_courses.keys()))


# ------------------------------------------------------------
# INHERITANCE
# ------------------------------------------------------------

class Instructor(User):

    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.courses_taught = []
        self.earnings = 0

    def create_course(self, title, price):
        course = Course(title, price, self)
        self.courses_taught.append(course)
        return course

    # POLYMORPHISM
    def display_info(self):
        print(f"👩‍🏫 Instructor: {self.name}")
        print("Courses Taught:", [c.title for c in self.courses_taught])


# ------------------------------------------------------------
# SUPPORTING CLASS
# ------------------------------------------------------------

class Course:

    # CLASS ATTRIBUTE
    platform_name = "Coursera"

    def __init__(self, title, price, instructor):
        self.title = title
        self.price = price
        self.instructor = instructor

    # INSTANCE METHOD
    def show_details(self):
        print(f"{self.title} | ₹{self.price} | Instructor: {self.instructor.name}")


class Certificate:

    def __init__(self, learner_name, course_name):
        self.__learner_name = learner_name   # PRIVATE
        self.__course_name = course_name     # PRIVATE

    def generate(self):
        print(f"🎓 Certificate Generated for {self.__learner_name} ({self.__course_name})")

    # STATIC METHOD (utility behavior)
    @staticmethod
    def verify_certificate():
        print("Certificate verified successfully")


# ------------------------------------------------------------
# CONTROLLER / MANAGER CLASS
# ------------------------------------------------------------

class CourseraPlatform:

    # CLASS ATTRIBUTE
    total_revenue = 0

    def __init__(self):
        self.users = []
        self.courses = []

    # CLASS METHOD
    @classmethod
    def platform_name(cls):
        return "Coursera LMS"

    # INSTANCE METHOD
    def register_user(self, user):
        self.users.append(user)
        print(f"{user.name} registered successfully")

    def add_course(self, course):
        self.courses.append(course)

    def list_courses(self):
        print("\nAvailable Courses:")
        for course in self.courses:
            course.show_details()

    # STATIC METHOD
    @staticmethod
    def show_platform_report():
        print("\n📊 Platform Report")
        print(f"Total Users: {User.total_users}")
        print(f"Total Revenue: ₹{CourseraPlatform.total_revenue}")


# ------------------------------------------------------------
# CLI DEMONSTRATION (Command Line Simulation)
# ------------------------------------------------------------

platform = CourseraPlatform()

print("\n===== Welcome to Coursera Learning Platform =====")

# -------- Register Instructor --------
print("\n--- Instructor Registration ---")
inst_name = input("Enter Instructor Name: ")
inst_email = input("Enter Instructor Email: ")
inst_password = input("Set Instructor Password: ")

instructor = Instructor(inst_name, inst_email, inst_password)
platform.register_user(instructor)

# -------- Register Learner --------
print("\n--- Learner Registration ---")
learner_name = input("Enter Learner Name: ")
learner_email = input("Enter Learner Email: ")
learner_password = input("Set Learner Password: ")

learner = Learner(learner_name, learner_email, learner_password)
platform.register_user(learner)

# -------- Instructor Creates Course --------
print("\n--- Course Creation ---")
course_title = input("Enter Course Title: ")
course_price = int(input("Enter Course Price: "))

course = instructor.create_course(course_title, course_price)
platform.add_course(course)

# -------- Display Courses --------
platform.list_courses()

# -------- Learner Enrollment --------
print("\n--- Course Enrollment ---")
learner.enroll_course(course)

# -------- Progress Update --------
print("\n--- Update Course Progress ---")
progress = int(input("Enter progress percentage (0–100): "))
learner.update_progress(course_title, progress)

# -------- Polymorphism Demonstration --------
print("\n--- Display User Information ---")
learner.display_info()
instructor.display_info()

# -------- Static & Class Method Demo --------
Certificate.verify_certificate()
CourseraPlatform.show_platform_report()