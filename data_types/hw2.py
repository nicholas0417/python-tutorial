def multiplication_or_sum(num1, num2):
  product = num1 * num2
  if(product < 1000):
    return product
  else:
    return num1 + num2

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))

result = multiplication_or_sum(number1, number2)
print("The result is", result)

"""
if a >= b + c or b>= a+c or c >= a+b:
 
    print("The triangle does not exist")
 
elif a==b and a==c:
 
    print ("Equilateral")
 
elif a==b or a==c or b==c:
 
    print ("Isosceles")
 
else:
 
    print("Obtuse")
"""