# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab3B.py
c1hrs = int(input("Course 1 hours: "))
c1grd = int(input("Grade for course 1: "))
c1QP = c1hrs * c1grd
c2hrs = int(input("Course 2 hours: "))
c2grd = int(input("Grade for course 2: "))
c2QP = c2hrs * c2grd
c3hrs = int(input("Course 3 hours: "))
c3grd = int(input("Grade for course 3: "))
c3QP = c3hrs * c3grd
c4hrs = int(input("Course 4 hours: "))
c4grd = int(input("Grade for course 4: "))
c4QP = c4hrs * c4grd
totalHrs = c1hrs + c2hrs + c3hrs + c4hrs
totalQP = c1QP + c2QP + c3QP + c4QP
GPA = float(round((totalQP / totalHrs), 2))
print("Total hours: " + str(totalHrs))
print("Total quality points: " + str(totalQP))
print("Your GPA for this semester is " + str(GPA))