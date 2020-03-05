###CTI-110
##P3T1 - Area of Rectangle
##Cory Lewis
##03/05/2020

##Input the length and width of recatangle 1.
##Input the length and width of rectangle 2.
##Calculate the area of rectangle 1.
##Calculate the are of rectangle 2.

##if area 1 > area 2
##    display "Rectangle 1 has the greatest area."
##else if area 2 > area 1
##    display "Rectangle 2 has the greatest area."
##else
##    display "Both rectangles have the same area."

print("Number value must be a whole number")

#Get the dimensions of Rectangle 1.
length1 = int(input("Enter the length of Rectangle 1: "))
width1 =int(input("Enter the width of Rectangle 1: "))

#Get the dimensions of Rectangle 2
length2 = int(input("Enter the length of Rectangle 2: "))
width2 = int(input("Enter the width of Rectangle 2: "))

#Calculate the area of the rectangle.
area1 = length1*width1
area2 = length2*width2

#Determine which has the greatest area.
if area1 > area2:
    print("Rectangle 1 has the greatest area. ")
elif area2 > area1:
    print("Rectangle 2 has the greatest area. ")
else:
    print("Both have the same area. ")


