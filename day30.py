#recursion in python
#factorial of a number
def fact(n):
    if (n==0 or n==1):
        return 1
    return n*fact(n-1)

n=int(input("Enter a number: "))
print("Factorial of the number is:", fact(n))
#fact(5) = 5*fact(4)
#fact(4) = 4*fact(3)
#fact(3) = 3*fact(2)
#fact(2) = 2*fact(1)
#fact(1) = 1

# fibonacci series
print("sum of Fibonacci series: ")
flag=0
def fib(n):

    # base case
    if (n==0 or n==1):
            return n
    else:
        return fib(n-1)+fib(n-2)



print(fib(n))