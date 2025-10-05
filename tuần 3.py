#1
a,b,c=input("enter numbers:").split()
reversed_a=int(str(a)[::-1])
reversed_b=int(str(b)[::-1])
reversed_c=int(str(c)[::-1])
print(f"{reversed_a} {reversed_b} {reversed_c}")
#2
a=121212
b=232323
a=a^b
b=a^b
a=a^b
print("a=",a)
print("b=",b)
#3
a=int(input("enter a number: "))
if a & (a-1)==0 and a!=0:
    print("TRUE")
else:
    print("FALSE")

#4
a,b=map(int,input("enter numbers: ").split())   
print("a//b",a//b)
#5
import math
a,b=map(int,input("enter numbers: ").split())
print(math.ceil(a/b))
#6
a=int(input("enter a number: "))
if a%2==0:
    print("even")   
else:
    print("odd")
#7
a,b=map(int,input("enter numbers: ").split())
if a <0 and b<0:
    print("yes") 
else:
    print("no")
#8
def so_sanh_chieu_dai(a, b):
    if len(a) > len(b):
        return True
    else:
        return False
print(so_sanh_chieu_dai(input("enter a string: "), input("enter another string: "))) 
#9
a,b,c=map(int,input("enter 3 sides of triangel:").split()) 
if a+b>c and a+c>b and b+c>a:
    print("yes")
else:
    print("no")
#10
a,b,c,d=map(int,input("enter 4 numbers:").split())
max=0
if a>b and a>c and a>d:
    max=a
elif b>a and b>c and b>d:
    max=b
elif c>a and c>b and c>d:
    max=c
else:
    max=d
print("max=",max)
#11
a,b,c=map(int,input("enter 3 sides of triangel:").split())
if a==b==c:
    print("tam giác đều")
elif a==b or b==c or a==c:
    print("tam giác cân")
else:
    print("tam giác thường")
#12
a=int(input("enter year: "))
if (a%4==0 and a%100!=0) or (a%400==0):
    print("năm nhuận")
else:
    print("năm không nhuận")
#13
a=int(input("số điện dùng trong tháng này(kwh) : ")) 
if a<=50:
    print("số tiền phải trả:",a*1500)
elif 50<a<=100: 
    print("số tiền phải trả:",50*1500+(a-50)*2000)
else:
    print("số tiền phải trả:",50*1500+50*2000+(a-100)*3000)
#14
a,b=input("enter numbers:").split()
#  nghiệm của ax + b = 0 là :
print(f"x={ (-int(b)/int(a)):.2f}")
#15
a=int(input("averge score: "))
if a>=8:
    print("giỏi")
elif 6.5<=a<8:
    print("khá")
elif 5<=a<6.5:
    print("trung bình")
else:
    print("yếu")
#16
x=float(input("enter a float number:"))
if x >= 0:
    floor = int(x)
else:
    floor = int(x) - 1
if x >= 0:
    ceil = int(x)+1
else:
    ceil=int(x)
if x >= 0:
    if (x - int(x)) >= 0.5:
        rounded = int(x) + 1
    else:
        rounded = int(x)
else:
    if (x - int(x)) <= -0.5:
        rounded = int(x) - 1
    else:
        rounded = int(x)
print(ceil, floor, rounded)
