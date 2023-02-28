def init_rows(length):
    rows = [["■"] * length for i in range(length)]
    return rows

def print_rows(rows):
    for i in range(3):
        for j in range(3):
            print(rows[i][j],end=" ")
        print()
    print()

def check_win(add_point):
    global rows
    for i in range(len(rows)):
        # 行の確認
        for j in range(len(rows)):
            if rows[i][j] != add_point:
                break
            else:
                if j == (len(rows) -1):
                    print("Game Over1")
                    rows = init_rows(len(rows))
                    return rows
        
        # 列の確認
        for j in range(len(rows)):
            if rows[j][i] != add_point:
                break
            else:
                if j == (len(rows) -1):
                    print("ok" + str(i) + str(j))
                    print("Game Over2")
                    rows = init_rows(len(rows))
                    return rows
    # 左上の斜め確認
    for i in range(len(rows)):
        if rows[i][i] != add_point:
            break
        else:
            if j == (len(rows) -1):
                print("Game Over3")
                rows = init_rows(len(rows))
                print_rows(rows)
                return rows
    # 右上の斜め確認
    for i in range(len(rows)):
        if rows[(i - len(rows))][i] != add_point:
            break
        else:
            if i == (len(rows) -1):
                print("Game Over4")
                rows = init_rows(len(rows))
                return rows
    
    for i in range(len(rows)):
        if "■"  in rows[i]:
            if i < (len(rows) -1):
                break
            else:
                print("yarinaosi")
                rows = init_rows(len(rows))
                return rows
        
            

rows = init_rows(3)
add_point = "o"

while True:
    column = int(input("列の数字を記入してください"))
    line = int(input("行の数字を記入してください"))
    if column > (len(rows) - 1) or line > (len(rows) - 1):
        print("不正なカラムが指定されています")
        continue

    print(column)
    if rows[column][line] == "■":
        rows[column][line] = add_point
    else:
        print("既に指定済みの場所になります")
        continue

    print_rows(rows)
    check_win(add_point)


    if add_point == "o":
        add_point = "x"
    else:
        add_point = "o"