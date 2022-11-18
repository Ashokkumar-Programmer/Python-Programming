'''
the problem we have given an array of integers. we need to like all the integers in the set and dislike all the 
ntegers in sets. your initial happiness is for each integer in the array if we add to happiness. 
otherwise, our happiness does not change. we need to output our final happiness at the end.
Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
'''
n, m = input().split()

sc_ar = input().split()

A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in sc_ar]))