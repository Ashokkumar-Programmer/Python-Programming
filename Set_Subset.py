'''
If set A is subset of set B, print True.
If set A is not a subset of set B, print False.
Sample Input

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Sample Output

True 
False
False
'''
n=int(input())
output=[]
for i in range(n):
	n1=int(input())
	inp1=list(map(int,input().split()))
	n2=int(input())
	inp2=list(map(int,input().split()))
	temp=0
	for i in range(n1):
		for j in range(n2):
			if inp1[i]==inp2[j]:
				temp+=1
				break
	if temp==n1:
		output.append("True")
	else:
		output.append("False")
print(*output,sep="\n")