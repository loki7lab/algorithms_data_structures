#************change******************
'''
lis = [1,5,20,50]
def change(lis,num):
    changelis = []
    for i in lis[::-1]:
        a = num // i
        num = num % i
        changelis.append(a)
    return changelis
print(change(lis,100))
'''
#recursive
'''
def recDC(coinValueList,change,knownResult):
    minCoins = change
    if change in coinValueList:
        return 1
    elif knownResult[change] > 0:
        return knownResult[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList,\
                                change - i,knownResult)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResult[change] = minCoins
        return minCoins

print(recDC([1,5,10,25],63,[0]*64))
'''
#dynamic programming
'''
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= change]:
            if cents - j >= 0:#there may be index < 0
                if minCoins[cents - j] + 1 <coinCount:
                    coinCount = minCoins[cents - j] + 1
                    newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin -= thisCoin

amnt = 10
clist = [1,5,10,21,25]
coinsUsed  = [0]*(amnt + 1)
coinCount = [0]*(amnt + 1)
print("Making change for",amnt,"requires")
print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
print("They are:")
printCoins(coinsUsed,amnt)
print("The used list is as follows:")
print(coinsUsed)
'''
#**************thief*****************
#dp
#without function
'''
tr = [None,{'w':2,'v':3},{'w':3,'v':4},{'w':4,'v':8},{'w':5,'v':8},{'w':9,'v':10}]

max_w = 20

m = {(i,w):0 for i in range(len(tr))
                for w in range(max_w + 1)}
#print(m)
for i in range(1,len(tr)):
    for w in range(1,max_w + 1):
        if tr[i]['w'] > w:
            m[(i,w)] = m[(i-1,w)]
        else:
            m[(i,w)] = max(
                m[(i-1,w)],
                m[(i-1,w-tr[i]['w'])] + tr[i]['v']
            )

print(m[(len(tr)-1,max_w)])

'''

#recursive
tr = {(2,3),(3,4),(4,8),(5,8),(9,10)}
max_w = 20

m = {}

def thief(tr,w):
    if tr == set() or w == 0:
        m[(tuple(tr),w)] = 0
        return 0
    elif (tuple(tr),w) in m:
        return m[(tuple(tr),w)]
    else:
        vmax = 0
        for t in tr:
            if t[0] <= w:
                v = thief(tr - {t},w - t[0]) + t[1]
                vmax = max(vmax,v)
        m[(tuple(tr),w)] = vmax
        return vmax
print(thief(tr,max_w))
