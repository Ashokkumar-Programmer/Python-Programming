'''
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country 
stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country 
stamps.

Find the total number of distinct country stamps

Sample Input

7
UK
China
USA
France
New Zealand
UK
France 
Sample Output

5
Explanation

UK and France repeat twice. Hence, the total number of distinct country stamps is 5 (five).
'''
n=int(input())
inp=[]
for i in range(n):
	inp.append(input())
output=[]
for i in inp:
	if i not in output:
		output.append(i)
print(len(output))