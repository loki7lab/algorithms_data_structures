#***********************1************************
def findAnagrams(s, p):
    s_len = len(s)
    p_len = len(p)
    l = []
    p_list = [0 for _ in range(26)]
    s_list = [0 for _ in range(26)]
    for i in p:
        p_list[ord(i) - ord('a')] = p_list[ord(i) - ord('a')] + 1
    i = 0
    while i <= s_len - p_len:
        for x in s[i:i + p_len]:
            s_list[ord(x) - ord('a')] = s_list[ord(x) - ord('a')] + 1
        if s_list == p_list:
            l.append(i)
        s_list = [0 for _ in range(26)]
        i = i + 1
    if len(l) == 0:
        return ['none']
    else:
        return l
 
s = input()
p = input()
print(*findAnagrams(s, p))

#*************************2***********************************
def topKFrequent(nums, k):
    dct = {}
    for x in nums:
        dct[x] = dct.get(x, 0) + 1
    result = sorted(dct.items(), key=lambda x: (-x[1],x[0]))
    result = [x[0] for x in result[:k]]
    print(*result)
 
 
lst = eval(input())
k = int(input())
topKFrequent(lst, k)

#***************************3******************************
def createHashTable(n):
    if n <= 2:
        return [None] * 2
    for i in range(2, n):
        if n % i == 0:
            n += 1
    else:
        return [None] * n


def insertNumbers(table, nums):
    lenth = len(table)
    result = []
    for i in nums:
        hashValue = i % lenth
        if i in table:
            result.append(table.index(i))
        elif table[hashValue] == None:
            table[hashValue] = i
            result.append(hashValue)
        else:
            for j in range(1, lenth):
                hashValue = (i + j * j) % lenth
                if table[hashValue] == None:
                    table[hashValue] = i
                    result.append(hashValue)
                    break
            else:
                result.append('-')

    print(*result)


n = int(input())
nums = list(map(int, input().split()))
table = createHashTable(n)
insertNumbers(table, nums)
