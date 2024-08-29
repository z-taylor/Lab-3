# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab3C.py
numSmall = int(input("Enter the number of small sandwiches: "))
numMed = int(input("Enter the number of medium sandwiches: "))
numLarge = int(input("Enter the number of large sandwiches: "))
numXlarge = int(input("Enter the number of extra-large sandwiches: "))
totalMin = numMed + numLarge + (numXlarge * 2)
totalSec = (numSmall * 30) + (numLarge * 15) + (numXlarge * 15)
minAdd = totalSec // 60
totalSec = totalSec - (60 * (totalSec // 60))
totalMin += minAdd
print("Total cooking time is "+ str(totalMin) +" minutes and "+ str(totalSec) +" seconds.")