def int_split_list(number):
    str_number = str(number)
    list_number = list(str_number)
    check_number = [int(x.strip()) for x in list_number]
    return check_number

def appearance_number(number):
    appear_number ={0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
    return appear_number[number]

def calc_number(number):
    result = 1
    for i in int_split_list(number):
        result *= appearance_number(i)
    return result

def check_number(number):
    list=[number]
    while True:
        a = calc_number(list[-1])
        if a in list:
            break
        else:
            list.append(a)
    return len(list)

print(check_number(123456))