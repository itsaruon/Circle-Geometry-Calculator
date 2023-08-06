import math


#User Input
x1 = float (input("Enter the x coordinate of the center of the circle: "))
y1 = float (input("Enter the y coordinates of the center of the circle: "))
x2 = float (input("Enter the x coordinate of a point on the circle: "))
y2 = float (input("Enter the y coordinate of a point on the circle: "))


#Distance Function
def distance(x1,y1,x2,y2):
    return math.sqrt ((x2-x1)**2+(y2-y1)**2)

#Radius Function
def radius (x1,y1,x2,y2):
    return distance(x1,y1,x2,y2)

#Circumference Function
def circumference(r):
    return 2*3.14*r


#Output
print("Circle Radius = ", radius(x1,y1,x2,y2))
print ("Circle Cirumference = ", circumference(radius(x1,y1,x2,y2)))
