def f(dict,key):
  if key in dict:
    print("key is exists")
  else:
    print("key does not exists")
dict={1:"re",2:"ne",3:"ka"}
key=int(input("enter a key"))
f(dict,key)
