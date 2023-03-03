def check(line, students):
    if students == 0:
        return 1
    
    cnt = 0
    for i in range(1,n):
        if line[i] < 0:
            if (line[i - 1]) != (students - 1)\
            and (line[i - 1]) != ((students + 1) % n)\
            and (line[(i + 1) % n])!= (students - 1)\
            and (line[(i + 1) % n])!= ((students + 1) % n):
                line[i] = students
                cnt += check(line, students-1)
                line[i] = -1
    return cnt

n=10
# def check(ary,m):
#     if m==0:#全員配置したら完了
#         return 1
#     cnt=0
#     for i in range(1,n):
#         #場所を順に調べる
#         if ary[i]<0:
#         # #未配置のとき
#             if(ary[i-1] != m - 1)\
#             and(ary[i - 1]!=(m + 1)%n)\
#             and(ary[(i + 1) % n]!=m - 1)\
#             and(ary[(i + 1) % n]!=(m + 1) % n):
#                 ary[i]=m
#                 cnt+=check(ary,m - 1)
#                 ary[i]= -1
#     return cnt


ary = [-1] * n
ary[0] = 0
print(check(ary, n-1))
