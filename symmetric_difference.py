'''
Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
Sample Output

5
9
11
12
'''
n1=int(input())
a=set(map(int,input().split()))
n2=int(input())
b=set(map(int,input().split()))
c=list(a.symmetric_difference(b))
c.sort()
print(*c,sep="\n")