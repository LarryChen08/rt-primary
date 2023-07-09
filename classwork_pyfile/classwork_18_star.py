
class CLS_star(object):
    def __init__(self, name, month1, day1, month2, day2, likelist):
        self.name = name
        self.month1 = month1
        self.day1 = day1
        self.month2 = month2
        self.day2 = day2
        self.likeList = likelist
    def is_in(self, month, day):
        if (month == self.month1) and (day >= self.day1):
            return True
        elif (month == self.month2) and (day <= self.day2):
            return True
        return False

def get_star_index(month, day):
    for i in  range(len(starList)):
        if starList[i].is_in(month, day):
            return i



starList = [CLS_star('白羊', 3, 21, 4, 19, [9, 2, 3]),
            CLS_star('金牛', 4, 20, 5, 20, [3, 5, 8]),
            CLS_star('双子', 5, 21, 6, 21, [7, 1, 10]),
            CLS_star('巨蟹', 6, 22, 7, 22, [3, 7, 5]),
            CLS_star('狮子', 7, 23, 8, 22, [2, 6, 8]),
            CLS_star('处女', 8, 23, 9, 22, [10, 3, 11]),
            CLS_star('天枰', 9, 23, 10, 23, [3, 7, 5]),
            CLS_star('天蝎', 10, 24, 11, 22, [10, 8, 6]),
            CLS_star('射手', 11, 23, 12, 21, [3, 5, 9]),
            CLS_star('魔蝎', 12, 22, 1, 19, [3, 9, 8]),
            CLS_star('水瓶', 1, 20, 2, 18, [7, 8, 9]),
            CLS_star('双鱼', 2, 19, 3, 20, [3, 0, 6])]

while True:
    month1, day1 = eval(input('请输入你的月日:'))
    star1Index = get_star_index(month1, day1)
    print('你的星座是' + starList[star1Index].name + '座')

    month2, day2 = eval(input('请输入对方的月日:'))
    star2Index = get_star_index(month2, day2)
    print('对方的星座是' + starList[star2Index].name + '座')

    if starList[star2Index].likeList[0] == star1Index:
        print('那个人想做你的小弟')
    elif starList[star2Index].likeList[0] == star1Index:
        print('那个人想做你的大哥')
    elif starList[star2Index].likeList[0] == star1Index:
        print('那个人想做你的小弟')
    else:
        print('那个人不想做你的小弟')


