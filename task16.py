#1)

def func_compute(y):
 return lambda x : x * y
result = func_compute(2)
print("multiply x by y is =", result(15))

#output

multiply x by y is = 30

[Program finished]


2)

from functools import reduce
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1]) 
print(fib(5)) 

# Output:
	
	[0, 1, 1, 2, 3]

[Program finished]

3)

nums = [2, 4, 6, 9 , 11]
n =int(input("Enter a number:"))
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

#output

Enter a number:4
Original list:  [2, 4, 6, 9, 11]
Given number:  4
Result:
8 16 24 36 44

[Program finished]

4)

lst = [67,65, 54, 36,108,126,144,339, 210,]
result = list(filter(lambda x: (x % 9 == 0), lst))
print("Numbers divisible by 9 are",result)

output

Numbers divisible by 9 are [54, 36, 108, 126, 144]

[Program finished]

5)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nEven numbers list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))

output

Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Even numbers list:
[2, 4, 6, 8, 10]

[Program finished]
