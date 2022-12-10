# Calculating the area of triangle using values of base and height.

base= float(input("Enter the base of the triangle: "))
height=float(input("Enter the height of the triangle: "))

area1=(base * height)/2
print('The area of triangle is: ' + str(area1) +"\n")

#Calculating the aea and semi perimeter of triangle using values of sides

a=float(input("Enter the value of 'a' side of triangle: \n"))
b=float(input("Enter the value of 'b' side of triangle: \n"))
c=float(input("Enter the value of 'c' side of triangle: \n"))

s=(a + b + c) / 2
area2=(s*(s-a)*(s-b)*(s-c)) ** 0.5

print('The area of triangle is: ' + str(area2))
print('The semi perimeter of triangle is: ' + str(s))