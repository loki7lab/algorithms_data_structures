#test 1
'''
s = eval(input())

def minstring(s):
    minstr = s
    for i in range(len(s)):
        s = s[1:]+s[0]
        if s < minstr:
            minstr = s
    return minstr
 
print(minstring(s))
'''

#test 2
# not ac
#坑：若存在相同元素，需要计入[后面]相同元素的个数

def func1(mylist):
    eventlist = []

    for i in range(len(mylist)):
        count = 0
        timeend = mylist[i]
        timestart = max(timeend-10000,0)
        j = i

        while timestart <= timeend:
            count += 1
            j -= 1 
            if j < 0:
                break
            else:
                timeend = mylist[j]

        eventlist.append(count)

    return eventlist



    

#other
'''
from pythonds.basic.queue import Queue

def func(mylist):
    """
    队列，先入队的第一个元素进行计算，然后再加入新的元素入队，
    同时循环判断队首元素-队尾元素是否大于10000
    若大于，除去队尾元素；否则返回队列长度
    坑：若存在相同元素，需要计入后面相同元素的个数
    """
    q = Queue()
    n = 0
    newlist = []#queue
    output = []
    for num in mylist:
        q.enqueue(num)
    while n < len(mylist):
        first = q.dequeue()#从尾端弹出【仅处理尾端
        newlist.append(first)
        while newlist[-1] - newlist[0]>5:#重复利用newlist
            newlist.pop(0)
        sum = 0
        print(q.items)#是q删除首位后，按应该顺序（mylist）的反序
        for i in reversed(q.items):   #队列翻转，若第一个不是，直接退出;为了防止踩坑
            if i == newlist[-1]:
                sum += 1
            else:
                break
        output.append(len(newlist)+sum)
        n += 1
    return output

'''
mylist = eval(input())
c1 = func1(mylist)


def func2(mylist):
    dic = dict()
    eventlist = []
    keyl = []
    valuel = []
    for my in mylist:
        if my not in dic:
            dic[my] = 1
        else:
            dic[my] += 1
    for key,value in dic.items():
        keyl.append(key)
        valuel.append(value)
    
    for i in range(len(keyl)):
        count = 0
        timeend = keyl[i]
        timestart = max(timeend-5,0)
        j = i
        while timestart <= timeend:
            count += valuel[j]
            j -= 1
            if j < 0:
                break
            else:
                timeend = keyl[j]
        eventlist.append(count)

    return eventlist


c2 = func2(mylist)

print(c2)
