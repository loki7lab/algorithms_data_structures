#**********10toStr*************
'''
def toStr(n,base):
    convertString = '0123456789ABCDEF'

    if n < base:#base condition
        return convertString[n]
    else:
        return toStr(n // base,base) + convertString[n % base]
#*********10toStrS(Stack)******
from pythonds.basic.stack import Stack
rStack = Stack()
def toStrs(n,base):
    convertString = '0123456789ABCEDF'
    if n < base:
        rStack.push(convertString[n])
        
    else:
        rStack.push(convertString[n % base])
        toStrs(n // base,base)
print(toStrs(256,2))
'''
#****************hanoi******************
'''
def moveTower(height,fromPole,withPole,toPole):
    if height >= 1:
        moveTower(height - 1,fromPole,toPole,withPole)
        moveDisk(height,fromPole,toPole)
        moveTower(height - 1,withPole,fromPole,toPole)
def moveDisk(disk,fromPole,toPole):
    print(f"Moving disk {disk} from {fromPole} to {toPole} ")

moveTower(5,"1#","2#","3#")
'''
#****************climbStairs**********
'''
def climbStairs(n):
    dp = {}
    dp[2] = 2
    dp[1] = 1
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(climbStairs(3))
'''
#backup
A = list(range(3))
for i in range(2):
    for j in range(10,A[i]-1,-1):
        print(i)
        print(j)
        print('***')