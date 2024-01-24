print("Enter the value of first number")
a = int(input())
print("Enter the value of second number")
b = int(input())

print("Enter the operations for calculation")
d = str(input())

if(d=="+"):
 print("The addition of first and second number is",a+b)
elif(d=="-"):
 print("The subtraction of first and second number is",a-b)
elif(d=="*"):
 print("The multiplication of first and second number is",a*b)
elif(d=="/"):
 print("the division of first and second number is",a/b)
else:
 print("You have enter wrong operator")
