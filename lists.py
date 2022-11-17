'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the 
7 types listed above.Iterate through each command in order and perform the corresponding operation on your list.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

'''
n=int(input())
l=[]
for i in range(n):
	inp=list(map(str,input().split()))
	command=inp[0]
	if command=="insert":
		l.insert(int(inp[1]),int(inp[2]))
	elif command=="print":
		print(l)
	elif command=="remove":
		l.remove(int(inp[1]))
	elif command=="append":
		l.append(int(inp[1]))
	elif command=="sort":
		l.sort()
	elif command=="pop":
		l.pop()
	elif command=="reverse":
		l.reverse()