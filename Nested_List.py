'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the 
name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print 
each name on a new line

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry

Explanation 0

There are 5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, 
so we order their names alphabetically and print each name on a new line.

'''
n=int(input())
inp=[]
for i in range(n):
	temp=[]
	inp1=input()
	inp2=float(input())
	temp.append(inp1)
	temp.append(inp2)
	inp.append(temp)
sort=[]
for i in range(n):
	sort.append(inp[i][1])
sort.sort()
sort1=[]
for i in sort:
	if i not in sort1:
		sort1.append(i)
second_lowest=sort1[1]
result=[]
for i in range(len(inp)):
	if inp[i][1]==second_lowest:
		result.append(inp[i][0])
result.sort()
print(*result,sep="\n")