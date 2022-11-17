'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2 
'''
inp=input()
output=""
for i in range(len(inp)):
	if inp[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
		output+=inp[i]
	if (inp[i].islower()):
		output+=inp[i].upper()
	if (inp[i].isupper()):
		output+=inp[i].lower()
print(output)