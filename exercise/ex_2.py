import math
# trojkat

a = 10
b = 20
c = 15
h = 12

obwod = a + b + c
pole = int((h * a) / 2)

print("Obwod trojkata wynosi " + str(obwod) + ", zas pole wynosi " + str(pole) + ".")

#prostokat
a = 10
b = 5
obwod = 2*a +2*b
pole = a * b

print ("Obwod prostokata wynosi " + obwod + ", a pole " + pole ".")

#kolo
r = 5
obwod = 2 * math.pi * r
pole = math.pi * r^2

print ("Obwod koła wynosi " + obwod + ", a pole " + pole ".")

#trapez
a = 6
b = 8
c = 3
h = 5
obwod = 2*c + a + b
pole = (a+b)/2 * h
print ("Obwod trapezu wynosi " + obwod + ", a pole " + pole ".")

#romb
a=5
d1 = 10
d2 = 7
obwod = 4*a
pole = d1 * d2 * 1/2
print ("Obwod rombu wynosi " + obwod + ", a pole " + pole ".")