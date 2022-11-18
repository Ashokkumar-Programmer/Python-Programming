'''
1 4
x**3 + x**2 + x + 1

'''
inp=list(map(int,input().split()))
x=inp[0]
k=inp[1]
inp1=input()
inp2=""
for i in range(len(inp1)):
	if inp1[i]=="x":
		inp2+=str(x)
	else:
		inp2+=inp1[i]
if eval(inp2)==k:
	print(True)
else:
	print(False)