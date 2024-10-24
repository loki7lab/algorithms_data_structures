#*********1.base************
'''
m,n = input().split()
m = int(m)#FROM
n = int(n)#TO
num = str(input())

strlist = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#change to 10

num10 = 0
for i in range(len(num)):
    num10 += m**(len(num)-i-1)*int(strlist.index(num[i]))

#num10 = int(num, base = m)

def toStr(n,num10):
    strlist = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #from 10 to any base
    if n > num10:
        return strlist[num10]
    else:
        return toStr(n,num10//n)+strlist[num10%n]

print(toStr(n,num10))
'''
#******************2.hanoi4#************************\
'''
def hanoi4(n):
    h_list = [0] * (n + 1)
 
    def f(m):
        if h_list[m]:#when h_list[m] = 1.because there is only one time for 1 pan.
            return h_list[m]
        result = 2 ** m - 1#3 hanoi
        for x in range(1, m):
            result = min(result, 2 * f(x) + 2 ** (m - x) - 1)#record the times when #pans <= m.x less than m for 37th row is calculating.
        h_list[m] = result
        return result
 
    return f(n)
print(hanoi4(int(input())))
'''
#**************
m,n = map(int,input().split())
print(type(m))