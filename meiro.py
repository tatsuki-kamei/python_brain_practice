maze=[
    [9,9,9,9,9,9,9,9,9],
    [9,0,0,0,9,9,0,9,9],
    [9,0,9,9,0,0,0,0,9],
    [9,0,0,0,0,9,9,9,9],
    [9,9,0,9,0,9,0,1,9],
    [9,0,0,9,0,0,0,9,9],
    [9,0,9,0,0,9,0,0,9],
    [9,9,9,9,9,9,9,9,9]
    ]



d=[[0,-1],[-1,0],[0,1],[1,0]]
#スタート位置をセット
x,y=1,1
#進行方向をセット
dir=0
# while maze[x][y]!=1:
#     print(dir)
#     move=d[(dir+1)%4]
#     print(move)
#     #進行方向の右側
#     if maze[x+move[0]][y+move[1]]!=9:
#         #壁でなければ移動し、進行方向を右に変える
#         dir=(dir+1)%4
#         x+=move[0]
#         y+=move[1]
#         print([x,y])
#     else:
#         #壁の場合は進行方向を左に変える
#         dir=(dir+3)%4

# def search(log):
#     x,y=log[-1]
#     if maze[x][y] == 1:
#         return len(log) - 1
    
#     depth = [99999]

#     for move in d:
#         if maze[x+move[0]][y+move[1]] != 9:
#             if [x+move[0], y+move[1]] not in log:

#                 log.append([x+move[0], y+move[1]])
#                 depth.append(search(log))
#                 log.pop(-1)
#                 print(log)
            
#     return min(depth)

# print(search([[1,1]]))

fw=[[1,1]]
bw=[[4,7]]

log_fw=[[1,1]]
log_bw=[[4,7]]

depth = 0

def search(queue,log):
    result = []
    for x,y in queue:
        for move in d:
            xd,yd = x+move[0],y+move[1]
            if maze[xd][yd]!=9:
                if [xd, yd] not in log:
                    log.append([xd, yd])
                    result.append([xd, yd])
    return result

def check_map(fw, bw):
    for i in bw:
        if i in fw:
            return True
    return False

while True:
    fw = search(fw,log_fw) 
    depth += 1
    if check_map(fw,bw):
        break
    print(fw)
    bw = search(bw,log_bw)
    depth += 1

    if check_map(fw,bw):
        break
    print(bw)
print(depth)