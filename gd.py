def gcd(x,y):
  if x==0:
    return y
  elif y==0:
    return x
  else:
    return gcd(y,x%y)
x=int(input("enter x value"))
y=int(input("enter y value"))
print("Gcd of",x,y,"is",gcd(x,y))
