def senko_get_comb_total(turn,point):
    # turn: 何回か
    # point: 現在で取得できる最高得点
    # （9回では足りてない点数を入れる1通りなので1を返す）
    
    if turn == 1:
        return 1
    
    result = 0
    for i in range(point+1):
        result += senko_get_comb_total(turn-1,point - i)
    
    return result

def after_9_turn_check(senko,kouko):
    senko_pattern = senko_get_comb_total(9,senko)

    if senko > kouko:
        kouko_pattern = senko_get_comb_total(9,kouko)

    else:
        # ８回時点で勝利
        kouko_pattern = senko_get_comb_total(8,kouko)

        # 9回まで実施

        for i in range(senko):
            kouko_pattern += senko_get_comb_total(8,i)
        
    return senko_pattern * kouko_pattern

print(after_9_turn_check(7,8))
