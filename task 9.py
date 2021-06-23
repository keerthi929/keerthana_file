#1 to add value2 for each element 

list=[34,56,78,32,98,23,45]
print("original list:",list)
new_list=[i+2 for i in list]
print("The new list is:",new_list)

#3 fibonacci series

n = int(input("Enter the value of n: "))
a = 0
b = 1
sum = 0
count= 1
print("Fibonacci Series:")
while(count<= n):
  print(sum)
  count += 1
  a = b
  b = sum
  sum = a + b
  
  #4  to check  number is armstrong or not

n = int(input('enter a number :'))
temp = n
sum =0
while(n>0):
  n1=n%10
  sum=sum + n1**3
  n = n//10
print(sum)
if(sum == temp):
    print('given number is armstrong')
else :
    print('given number is not armstrong')
    
#5 multiplication tqble of 9
    
n=int(input("Enter a number:"))
for i in range(1, 11):
  print(n,'x',i,'=',n*i)
  
  
#6 to print days to ages 

days= int(input("Enter no of days:"))
Age= days / 365
print("Age is: ",Age)

#7 to check positive or negative
num=float(input("Enter a number :"))
if num>0:
   print(num,"is positive Number")
else:
	print(num,"is Negative Number")
	

#8to solve trignometric problems

import math
a=math.pi/3
print(math.sin(a))
print(math.tan(a))
print(math.cos(a))

# 9 calculator to solve basic arithmetic operations 

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")

