#Q1
x=int(input("please enter a munber:"))
y=int(input("please enter a munber:"))
product=x*y
if(product <= 1000):
        print(product)
else:
        print(x+y)

#Q2
print("determine triangle!")
a=int(input("side_a:"))
b=int(input("side_b:"))
c=int(input("side_c:"))
if( a+b<c or a+c<b or b+c<a ):
        print("Triangle dosen't exist!")
elif(a==b and b==c):
        print("This triangle is equilateral.")
elif(a==b or a==c or b==c):
        print("This triangle is isosceles.")
else:
        print("This triangle is obtuse.")
