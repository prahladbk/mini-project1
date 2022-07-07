from math import sqrt
print("progrm to calculate area of triangle")
a=int(input("ENTER THE VALUE OF SIDE A= "))
b=int(input("ENTER THE VALUE OF SIDE B= "))
c=int(input("ENTER THE VALUE OF SIDE C= "))
s=(a+b+c)/2

area=sqrt(s*(s-a)*(s-b)*(s-c))
print("AREA OF TRIANGLE=",area)
