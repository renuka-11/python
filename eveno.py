l=[]
n=int(input("enter no of elements"))
for i in range(n):
  ele=int(input("enter the elements"))
  l.append(ele)
even=[]
odd=[]
for i in range(n):
  if l[i]%2==0:
    even.append(l[i])
  else:
    odd.append(l[i])
print("even list",even)
print("odd list",odd)
