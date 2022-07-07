from math import sqrt
print("PROGRAM TO FIND ROOT")
a=int(input("enter the value of A:"))
b=int(input("enter the value of B:"))
c=int(input("enter the value of C:"))
d=(b*b)-(4*a*c)
print(d)
if d==0 :
 r=-b/(2*a)
 print("root=",r)
elif d>0 :
 r1=(-b+sqrt(d))
 r2=(-b-sqrt(d))
 print("r1=",r1)
 print("r2=",r2)
elif d<0 :
 print("no real roots")

