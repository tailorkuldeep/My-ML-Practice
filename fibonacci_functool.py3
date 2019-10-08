from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
	if(type(n) != int):
		raise TypeError(" n must be a positive integer")
	if(n < 1):
		raise ValueError("n must be positive integer")
	 if n < 2 :
	 	return n
	 return fib(n-1) + fib(n-2)
num = int(input("Enter no of terms in Fibonacci series: "))
for i in range(num):
	print(fib(i),end=" ")

print("\n",fib.cache_info())
