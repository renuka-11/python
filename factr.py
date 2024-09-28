def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
n=int(input("enter a number"))
if n<0:
  print("factorial does not exists")
else:
  print("factorial of n is",fact(n))
