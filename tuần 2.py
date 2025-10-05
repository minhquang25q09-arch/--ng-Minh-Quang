#W2A3
a = int(input(" number 1: "))
b = int(input(" number 2: "))
print(a + b, a-b, a*b, a//b, a%b)
print(f"{a/b:.2f}")
#W2A4
a, b, c, x, y, z= input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(x)
e = int(y)
f = int(z)
avg = (a + b + c + (d+e)*2 + f*3) / 10
print(f" your avg: {avg/10:.2f} ")
#W2A5
a,b = input().split()
a = int(a)
b = int(b)
print(f"{a**b}")
#W2A6
a = str(input()).upper()
print(a)
#W2A7
print(((13**2)*3) + 5)
print(13**(2*3) + 5 )
#W2A8
a = float(input("nhiệt độ c "))
print(f"nhiệt độ F: {a*1.8 + 2} ")
#W2A9
x = int(input("Enter price: "))
print(f" real price: {10 + x*1.4}")
#W2A11
a = int(input("Enter time: "))
print(f"timer: {a//3600} hours {a%60} minutes {a%60} seconds")
#W2A12
n = int(input("Enter time: "))
print(f"Amount of textiles: {n**2 * 6}")
#W2A13
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
LastDigit = int(str(a*b)[-1])
print(f"your last digit is: {LastDigit} ")
#W2A14
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
a,b = b,a
print(f"{a},{b}")
#W2A15
n = int(input("Enter number: "))
print(f" orbs' amount: {6*n*(n-1)+1}")