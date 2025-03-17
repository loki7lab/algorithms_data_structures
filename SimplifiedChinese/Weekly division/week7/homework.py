#**********************1****************************
l = list(map(int,input().split()))
length = len(l)
ll = []
if len(l) == 1:
    print(1)
    print(l[0])
else:
    for i in range(1,length-1):
        if l[i] > max(l[:i]) and l[i] < min(l[i+1:]):
            ll.append(l[i])
    if l[0] < l[1]:
        ll.append(l[0])
    if l[-1] > l[-2]:
        ll.append(l[-1])
    ll.sort()
    print(len(ll))
    print(" ".join([str(i) for i in ll]))

#***********************2*******************************

N = int(input())
isBadVersion = eval(input())
 
def firstBadVersion(n):
   left = 1
   right = n
   while(left<right):
       mid = left + (right - left) //  2
       if (isBadVersion(mid)):
           right = mid
       else:
           left = mid + 1
   return left
 
print(firstBadVersion(N))

#*****************************3**********************************
def check(lst1,lst2):
    flag = 0
    for i in range(len(lst2)-1):
        if lst2[i] > lst2[i+1]:
            flag = i + 1
            break
    if lst1[flag:] == lst2[flag:]: # 插入排序
        result = sorted(lst1[:flag+1])+lst2[flag+1:] # 再迭代一轮的结果
        return True,result
    else: # 归并排序
        cnt = 2 # 归并的数量
        result = lst2
        while result == lst2: # 不断归并排序直到顺序发送变化
            sub_lst = [sorted(lst2[i:i+cnt]) for i in range(0,len(lst2),cnt)]
            result = [num for sub in sub_lst for num in sub]
            cnt *= 2
        return False,result
 
 
lst1 = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]
num = len(lst1)
flag,next_list = check(lst1,lst2)
if flag:
    print("Insertion Sort")
else:
    print("Merge Sort")
print(" ".join([str(i) for i in next_list]))