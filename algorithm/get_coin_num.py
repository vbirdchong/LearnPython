#!/usr/bin/env python
# coding=utf-8

'''
以人民币的硬币为例，假设硬币数量足够多。要求将一定数额的钱兑换成硬币。要求兑换硬币数量最少。

这是用贪婪算法的典型应用。在本例中用python来实现，主要思想是将货币金额除以某硬币单位，然后去整数，即为该硬币的个数；余数则做为向下循环计算的货币金额。

这个算法的问题在于，得出来的结果不一定是最有结果。比如，硬币单位是[1,4,6],如果将8兑换成硬币，按照硬币数量最少原则，应该兑换成为两个4（单位）的硬币，
但是，按照本算法，得到的结果是一个6单位和两个1单位的硬币。这也是本算法的局限所在。所谓贪婪算法，本质就是只要找出一个结果，不考虑以后会怎么样。
'''

def get_coin_result(money):
    # 硬币单位 1分 2分 5分 1角 2角 5角 1元
    coin_type = [1, 2, 5, 10, 20, 50, 100]
    # 单位从大到小排列
    coin_type.sort(reverse=True)

    # 化成分为单位
    money = money * 100

    coin_details = {}

    for unit in coin_type:
        num_coin = money // unit
        if num_coin > 0:
            coin_details[unit] = num_coin

        remain_money = money % unit
        if (0 == remain_money):
            break
        else:
            money = remain_money
    return coin_details

if __name__ == "__main__":
    money = 3.24
    coin_detail_num = get_coin_result(money)
    print coin_detail_num

    detail_result = [(coin_type, coin_detail_num[coin_type]) for coin_type in sorted(coin_detail_num.keys())]
    print detail_result

    print "The money {}RMB will changed by like as:".format(money)
    print "Coin         Num"
    for i in detail_result:
        if i[0] == 100:
            print "Yuan     {}  {}".format(i[0]/100, i[1])
        elif i[0] < 10: 
            print "Fen      {}  {}".format(i[0], i[1])
        else:
            print "Jiao     {}  {}".format(i[0]/10, i[1])
                        
        


# 最小硬币法
def coinChange(centsNeeded, coinValues):
    minCoins = [[0 for j in range(centsNeeded + 1)] for i in range(len(coinValues))]
    minCoins[0] = range(centsNeeded + 1)

    for i in range(1,len(coinValues)):
        for j in range(0, centsNeeded + 1):
            if j < coinValues[i]:
                minCoins[i][j] = minCoins[i-1][j]
            else:
                
                minCoins[i][j] = min(minCoins[i-1][j], 1 + minCoins[i][j-coinValues[i]])
    return minCoins[-1][-1]



