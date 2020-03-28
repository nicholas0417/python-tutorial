# Q2
a = int(input("side_a:"))
b = int(input("side_b:"))
c = int(input("side_c:"))
if ( a+b<c or a+c<b or b+c<a ):
        print("Triangle dosen't exist!")
elif ( a==b and b==c ):
        print("This triangle is equilateral.")
elif ( a==b or a==c or b==c ):
        print("This triangle is isosceles.")
else:
        print("This triangle is obtuse.")