n1=int(input())
inp1=list(map(int,input().split()))
n2=int(input())
inp2=list(map(int,input().split()))
output=[]	
for i in range(len(inp1)):
	for j in range(len(inp2)):
		if inp1[i]==inp2[j]:
			output.append(inp1[i])
			break
print(len(output))