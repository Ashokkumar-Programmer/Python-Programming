'''
Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Sample Input 1

2
2
2
2
Sample Output 1

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], 
[1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], 
[2, 2, 0], [2, 2, 1], [2, 2, 2]]

'''
tempinp=""
max1=[]
for i in range(3):
	temp=input()
	max1.append(temp)
	tempinp+=temp
n=int(max(max1))
condition=int(input())
inp=int(tempinp)
str1=[]
sum1=0
for i in range(inp+1):
	temp=[]
	n1=len(str(sum1))
	a=0
	b=0
	c=0
	if n1==1:
		if (0+0+sum1)!=condition and (sum1<=n):
			temp.append(0)
			temp.append(0)
			temp.append(sum1)
	if n1==2:
		a=sum1//10
		b=sum1%10
		if (0+a+b)!=condition and (a<=n and b<=n):
			temp.append(0)
			temp.append(a)
			temp.append(b)
	if n1==3:
		a=(sum1//10)//10
		b=(sum1//10)%10
		c=sum1%10
		if (a+b+c)!=condition and (a<=n and b<=n and c<=n):
			temp.append(a)
			temp.append(b)
			temp.append(c)
	if len(temp)!=0:
		str1.append(temp)
	sum1+=1
print(str1)