def split_number(number):
    x = 1
    list=[]
    while True:
        x += 1
        if number <= x:
            list.append(number)
            break
        else:
            while number % x == 0:
                number //= x
                list.append(x)
    return list

print('x'.join(str(i) for i in split_number(123456789)))