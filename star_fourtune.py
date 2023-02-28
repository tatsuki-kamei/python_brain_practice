def check_stars(month, day):
    stars = ['山羊座','水瓶座','魚座','牡羊座','牡牛座','双子座','蟹座','獅子座','乙女座','天秤座','蠍座','射手座']
    ajust_month= [19,18,20,19,20,21,22,22,22,23,22,21]
    if ajust_month[((month % 12) - 1)] < day:
        return stars[((month % 12))]
    else:
        return stars[(month % 12) - 1]