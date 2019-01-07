from functools import lru_cache
import time
import matplotlib.pyplot as plt
import seaborn as sns
f={}

def fibc(n):
	 if n < 2 :
	 	return n
	 return fibc(n-1) + fibc(n-2)
def fibd(n):
	if(n in f):
		return f[n]
	if(n == 1):
		v=1
	if(n == 2):
		v=2
	elif(n>2):
		v = fibd(n-1) + fibd(n-2)
	f[n]=v
	return v
print("using dictionary")
num = 10
z=[]
while(num<=100):
	st=time.time()
	for i in range(1,num+1):
		fibd(i)
	et=time.time()
	z.append(et-st)
	#print(et-st)
	num+=10
print(z)

@lru_cache(maxsize=None)
print("using caching")
num = 10
x=[]
y=[]
while(num<=100):
	st=time.time()
	for i in range(1,num+1):
		fibc(i)
	et=time.time()
	x.append(et-st)
	y.append(num)
	#print(et-st)
	num+=10
print(x)

ax= sns.stripplot(y,x)
bx= sns.stripplot(y,z)
ax.set(xlabel="num" , ylabel="time")
plt.title("graph b/w no n time taken to calculate fib ")
plt.show()
print("\n",fibc.cache_info())
