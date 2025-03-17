#*********1.瓷砖***************
def tile(sizeList, space, knownResults):
    if space == 0:
        return 1
    elif knownResults[space] != 0:
        return knownResults[space]
    else:
        num = 0
        for i in [t for t in sizeList if t <= space]:
            num = num + tile(sizeList, space - i, knownResults)
            knownResults[space] = num
    return num


sizeList = [1, 2, 3, 4]
space = eval(input())
knownResults = [0] * (space + 1)
print(tile(sizeList, space, knownResults))
#*******************2.分糖果******************
def candy(ratings):
    sum = 0
    rewardList = [1] * len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            rewardList[i] = rewardList[i - 1] + 1
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and rewardList[i] <= rewardList[i + 1]:
            rewardList[i] = rewardList[i + 1] + 1
    for i in range(len(ratings)):
        sum += rewardList[i]
    # print(rewardList)
    return sum


lst = eval(input())
print(candy(lst))

#**************3.求值*******************
def findWays(expr):
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)

    def calc(nums, ops):
        if not ops:
            return [nums[0]]
        elif len(ops) == 1:
            if ops[0] == '+':
                return [nums[0] + nums[1]]
            if ops[0] == '-':
                return [nums[0] - nums[1]]
            else:
                return [nums[0] * nums[1]]
        else:
            res = []
            for i in range(len(ops)):
                for num1 in calc(nums[:i + 1], ops[:i]):
                    for num2 in calc(nums[i + 1:], ops[i + 1:]):
                        res.append(calc([num1, num2], [ops[i]])[0])

            return list(set(res))

    return calc(nums, ops)


expr = input()
a = findWays(expr)
a.sort()
print(','.join(str(i) for i in a))

