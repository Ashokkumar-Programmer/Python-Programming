n=int(input())
inp = list(map(int, input().split()))
inp.sort()
inp.reverse()
new_list = []
for one_student_choice in inp:
    if one_student_choice not in new_list:
        new_list.append(one_student_choice)
print(new_list[1])
