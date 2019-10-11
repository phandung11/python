import math
a=float(input())
b=float(input())
c=float(input())
print("canh dai nhat:",max(a,max(b,c)))
print("chu vi:",a+b+c)
x=(a+b+c)/2
print("dien tich:",math.sqrt(x*(x-a)*(x-b)*(x-c)))