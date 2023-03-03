score=[[9,1],[8,2],[10],[5,0],[3,6],[4,2],[7,3],[6,3],[10],[9,1,9]]



# total = 0
# x = 0
# y = 0
# while len(score) > 0:
#     number = score.pop(-1)
#     check = 0
#     for i in number:
#         print(total)
#         total += i
#         check += i
#         if check == 10:
#             if i == 10:
#                 total += x+y
#             else:
#                 total += x
#     if number[0] == 10:
#         y = x
#         x = number[0]
#     else:
#         x = number[0]
#         y = number[1]


def cacl(score):
    result,score1,score2 = 0,0,0
    while len(score) > 0:
        number = score.pop(-1)
        total = sum(number)
        if len(number) == 3:
            result += total
            score1,score2,_ = number
        elif len(number) == 1:
            result += 10 + score1 + score2
            score1,score2 = 10,score1
        elif total == 10:
            result += 10 + score1
            score1,score2 = number
        else:
            result += total
            score1,score2 = number
        
    return result

print(cacl(score))