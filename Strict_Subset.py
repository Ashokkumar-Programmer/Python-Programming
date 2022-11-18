'''
Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output 0

False
'''
def isstrictsuperset(a,b):
    return b.issubset(a) and not(a.issubset(b))
a = set(int(x) for x in input().split(' '))
n = int(input())
res = True
for _ in range(n):
    b = set(int(x) for x in input().split(' '))
    res &= isstrictsuperset(a,b)
print(res)