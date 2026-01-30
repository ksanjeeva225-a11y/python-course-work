print("Welcome! to COURSES ON COURSERA")
print("-----------------------------------")

# Task 1: Input Collection

course_id = int(input("Enter Course ID: "))
course_name = input("Enter Course Name: ")
course_price = float(input("Enter Course Price: "))

# Categories as list (no loop)
categories = input("Enter Course Categories: ")
course_categories = categories.split(",") 

course_progress = float(input("Enter Course Progress Percentage: "))

# Assessment scores as list of floats (no loop)
scores = input("Enter Assessment Scores: ")
assessment_scores = scores.split(",")

completed_assignments = int(input("Enter Completed Assignments: "))
total_assignments = int(input("Enter Total Assignments: "))
assignment_tuple = (completed_assignments, total_assignments)

# Certificates as set (no loop)
raw_certificates = input("Enter Earned Certificates: ")
course_certificates = set(raw_certificates.split(","))

# Instructor details (dict)
instructor_name = input("Enter Instructor Name: ")
instructor_contact = input("Enter Instructor Contact Email: ")
instructor_location = input("Enter Instructor Location: ")

instructor_details = {
    "name": instructor_name,
    "contact": instructor_contact,
    "location": instructor_location
}

# Task 2: Display with all formatting methods
print("\nCoursera Course Information:")
print("-----------------------------------")

# 1. Using comma separation
print("Course ID, Name, Price:", course_id, course_name, course_price, sep=", ")

# 2. Using percentage formatting
print("Course Progress: %.2f%%" % course_progress)

# 3. Using f-strings
print(f"Course Name: {course_name}")
print(f"Price: ${course_price:.2f}")
print(f"Assessments Entered: {assessment_scores}")
print(f"Assignments Completed: {assignment_tuple[0]} out of {assignment_tuple[1]}")
print(f"Certificates Earned: {course_certificates}")

# 4. Using .format() method
print("Instructor Details: Name - {}, Contact - {}, Location - {}".format(
    instructor_details["name"],
    instructor_details["contact"],
    instructor_details["location"]
))

print("-----------------------------------")
