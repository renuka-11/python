def fib(n):
  if n<=1:
    return n
  else:
    return (fib(n-1)+fib(n-2))
a=int(input("enter a value"))  
if a<=0:
  print("enter a positive number")
else:
  print("fibonacci series")
  for i in range(a):
    print(fib(i))
