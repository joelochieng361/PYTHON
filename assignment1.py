# Assignment
# 1. Write a python program that is able to calculate the BMI of a person whose weight is 78kgs and height is 1.75 meters. BMI = (weight) / (height squared)
# 2. Find the Area and perimeter of a rectangle whose length is 48cm and width is 25cm
# Research on python list, tuple and Dictionary Data types.

#assignment one
weight = 78
height = 1.75
heightsquared = height * height
BMI= weight / heightsquared
# generate output
print("The BMI fir the values is", BMI)

# Area and Perimeter- rectangle  length=48 width=25
length = 48
width = 25
# area
Area = length * width
print("Area of the rectangle is", Area)
perimeter = 2 * (length + width)
# perimeter
print("perimeter of the rectangle is", perimeter)