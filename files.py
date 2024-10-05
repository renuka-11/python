lines=[
	"first\n",
	"second\n",
	"third\n",
	]
f=open("example.txt",'w')
f.writelines(lines)
f.close()
f=open("example.txt",'r')
print(f.read())
f.close

