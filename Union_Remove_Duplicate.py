n1=int(input())
inp1=list(map(int,input().split()))
n2=int(input())
inp2=list(map(int,input().split()))
for i in inp2:
	inp1.append(i)
output=[]
for i in inp1:
	if i not in output:
		output.append(i)
print(len(output))