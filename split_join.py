'''
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen

Sample Input

this is a string   
Sample Output

this-is-a-string
'''
inp=input()
output=""
for i in range(len(inp)):
	if inp[i]==" ":
		output+="-"
	else:
		output+=inp[i]
print(output)