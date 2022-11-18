'''
Sample Input

3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
Sample Output

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle

'''
n=int(input())
inp=[]
output=[]
for i in range(n):
		inp.append(list(map(str,input().split())))
for i in range(len(inp)):
	if inp[i][3]=="M":
		output.append("Mr. {} {}".format(inp[i][0],inp[i][1]))
	elif inp[i][3]=="F":
		output.append("Ms. {} {}".format(inp[i][0],inp[i][1]))
print(output)
'''
import operator

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\\n')
'''