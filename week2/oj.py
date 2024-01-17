
# 1. 给出两个整数，输出他们的商
'''
a = int(input())
b = int(input())
if b != 0:
    print('%.3f'%(a/b))
else:
    print('NA')
'''
#给出行数和列数，打印一个由*号构成的实心矩形
'''
m,n = map(int,input().split())
for i in range(m):
    print('*'*n)
'''
# 给定若干个整数，找出这些整数中最小的，输出。
a = list(map(int,input().split()))
print(min(a))
