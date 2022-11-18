n=int(input())
inp=set(map(int,input().split()))
lc=int(input())
for i in range(lc):
	commands=list(map(str,input().split()))
	input_command=commands[0]
	if input_command=="pop":
		try:
			inp.pop()
		except:
			pass
	elif input_command=="remove":
		try:
			inp.remove(int(commands[1]))
		except:
			pass
	elif input_command=="discard":
		try:
			inp.discard(int(commands[1]))
		except:
			pass
print(sum(inp))