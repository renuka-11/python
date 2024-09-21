def f(l):
  ele=[]
  for i in l:
    if isinstance(i,list):
      ele.extend(f(i))
    else:
      ele.append(i)
  return ele
l=[1,2,3,[4,5,6],7]
print(f(l))
