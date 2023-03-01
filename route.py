def search(x, y):
    print(x)
    print(y)
    if x >= w:
        return search(0, y+1)
    
    if y >= h:
        return route[w-1][h-1]
    
    if y > 0:
        route[x][y] = route[x][y-1]
        print(route)
    
    if x > 0:
        route[x][y] = route[x-1][y]
        print(route)


    return search(x+1, y)

w,h = 2,3
route = [[0]*h for i in range(h)]
route[0][0] = 1
n= search(1,0)
print(n)