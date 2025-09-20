
# --- Personal Info ---
Full_name = "Charlestone Mayenga"
Student_email = "cjmayenga@ncat.edu"
Hometown = "Graham, NC"
Graduation_semester = "Spring 2027"
Major = "Computer Science"

# --- Academic Data ---
Current_courses = ["COMP 163", "MATH 341", "ENG 211", "COMP 180", "SPCH 250", "COMP 121"]
Completed_course = ["Psychology", "Chemistry", "Calculus", "Micro Economics","Macro Economic","World History"]
Credit_hours = [3, 3, 3, 3, 3, 3]
GPA_history = [4.0, 4.0, 3.7, 3.6]

# --- Contacts ---
Emergency_contact = ("Aunt", "Tausi Brooks", "336-555-0199")
Home_address = ("1060 Watercourse cirle", "Graham, NC, 27253")
Instagram_info = ("Instagram", "@cj_tonnt", "502")
Twitter_info = ("Twitter", "@cj_tonny", "58")
Birthday = ("Birthday", 5, 21, 2002)

# --- Interests ---
Current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
Career_interest = {"Software development", "Web development", "Data science", "Game development"}
Hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
Entertainment_backlog = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

# --- Organization ---
Course_credits = {"COMP 163": 3, "MATH 341": 3, "ENG 211": 3, "COMP 180": 3, "SPCH 250": 3, "COMP 121": 1}
course_professors = {
    "COMP 163": "Prof. Rhodes",
    "MATH 341": "Prof. Kurepa",
    "ENG 211": "Dr. White",
    "COMP 121": "Prof. Rhodes",
    "COMP 180": "Prof. Pioro",
    "SPCH 250": "Prof. Russell",
}
course_rooms = {
    "COMP 163": "M-Eric 300",
    "MATH 341": "Marteena 214",
    "ENG 211": "General CB 211",
    "SPCH 250": "Frye Hall 210",
    "COMP 121": "Graham 210",
    "COMP 180": "M-Eric 202",
}
Monthly_budget = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
Study_hours_per_subject = {"Programming": 10, "Math": 8, "English": 3, "Speech Fundamental": 2, "Discrete Structure": 6}
Contact_directory = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-500"}

# --- Calculations ---
Total_current_credits = sum(Course_credits.values())
Cumulative_gpa = sum(GPA_history) / len(GPA_history)
Completed_courses_count = len(Completed_course)
Total_study_hours = sum(Study_hours_per_subject.values())
Academic_load = Total_current_credits + Total_study_hours
Monthly_budget_total = sum(Monthly_budget.values())
Daily_food_budget = round(Monthly_budget["Food"] / 30, 2)
Annual_budget_projection = Monthly_budget_total * 12
Study_cost_per_hour = round(Monthly_budget["Books"] / Total_study_hours, 2)
Total_social_media_followers = int(Instagram_info[2]) + int(Twitter_info[2])
Contact_directory_size = len(Contact_directory)
Entertainment_backlog_count = len(Entertainment_backlog)

# ================================================================
# OUTPUT FORMATTING TO MATCH LAYOUT
# ================================================================

print("="*64)
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("="*64)

# --- Personal Info ---
print("Student:", Full_name, "|Email:", Student_email)
print("From:", Hometown, "|Graduating:", Graduation_semester)
print("Major:", Major)
print()

# --- Academic Profile ---
print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {Total_current_credits} credits across {len(Current_courses)} courses")
print(f"Cumulative GPA: {Cumulative_gpa:.2f}")
print(f"Weekly Study Time: {Total_study_hours} hours")
print(f"Academic Investment: ${Study_cost_per_hour} per study hour")
print()

print("Current Courses:")
print(f"COMP 163 - {Course_credits['COMP 163']} credits - {course_professors['COMP 163']} - {course_rooms['COMP 163']}")
print(f"MATH 341 - {Course_credits['MATH 341']} credits - {course_professors['MATH 341']} - {course_rooms['MATH 341']}")
print(f"ENG 211 - {Course_credits['ENG 211']} credits - {course_professors['ENG 211']} - {course_rooms['ENG 211']}")
print(f"SPCH 250 - {Course_credits['SPCH 250']} credits - {course_professors['SPCH 250']} - {course_rooms['SPCH 250']}")
print(f"COMP 180- {Course_credits['COMP 180']} credits - {course_professors['COMP 180']} - {course_rooms['COMP 180']}")
print(f"COMP 121 - {Course_credits['COMP 121']} credits - {course_professors['COMP 121']} - {course_rooms['COMP 121']}")
print()
# --- Personal Development ---
print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {Current_skills}")
print(f"Learning Goals: {skills_to_learn}")
print(f"Career Interests: {Career_interest}")
print(f"Skills Currently Have: {len(Current_skills)}")
print(f"Skills Want to Learn: {len(skills_to_learn)}")
print()
# --- Financial Overview ---
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${Monthly_budget_total}")
print(f"Food: ${Monthly_budget['Food']} (${Daily_food_budget}/day)")
print(f"Entertainment: ${Monthly_budget['Entertainment']}")
print(f"Books: ${Monthly_budget['Books']}")
print(f"Transportation: ${Monthly_budget['Transportation']}")
print(f"Annual Projection: ${Annual_budget_projection}")
print()
# --- Connections & Contacts ---
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {Emergency_contact[1]} ({Emergency_contact[0]}) - {Emergency_contact[2]}")
print(f"Home Address: {Home_address[0]}, {Home_address[1]}")
print(f"Social Media Presence: {Total_social_media_followers} followers across 2 platforms")
print(f"Key Contacts: {Contact_directory_size} people in directory\n")

# --- Life Statistics ---
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {Completed_courses_count}")
print(f"Current Academic Load: {Academic_load} weekly commitments")
print(f"Entertainment Backlog: {Entertainment_backlog_count} items")
print(f"Current Hobbies: {len(Hobbies)} activities")
print("="*64)