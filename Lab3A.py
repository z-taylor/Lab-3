# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab3A.py
AmntOwed = float(input("Amount owed: $"))
APR = round(float(input("APR: ")), 2) / 100
MonthlyPrcnt = round((APR*100/12), 3)
MinPmnt = round((AmntOwed*APR/12), 2)
print("Monthly percentage rate: " + str(MonthlyPrcnt))
print("Minimum payment: $" + str(MinPmnt))