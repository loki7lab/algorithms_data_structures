'''
def func(mylist):
    dic = dict()
    eventlist = []
    keys = []
    values = []
    for my in mylist:
        dic[my] = dic.get(my,0)+1
    for key,value in dic.items():
        keys.append(key)
        values.append(value)
    
    for i in range(len(keys)):
        count = 0
        timeend = keys[i]
        timestart = max(timeend-10000,0)
        j = i
        while timestart <= timeend:
            count += values[j]
            j -= 1
            if j < 0:
                break
            else:
                timeend = keys[j]
        eventlist.append(count)

    return eventlist

mylist = eval(input())
print(list(func(mylist)))
'''
#********************************
'''
from pythonds.basic import Queue
def hotpotato(namelist,num):
    simque = Queue()
    for name in namelist:
        simque.enqueue(name)
    while simque.size() > 1:
        for i in range(num):
            simque.enqueue(simque.dequeue())
        simque.dequeue
    return simque.dequeue()
'''
#************************************
'''
from pythonds.basic import Deque
def palchecker(astring):
    chardeque = Deque()

    for ch in astring:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual
'''
#*****
'''
def func(S):
    output = S
    simqueue = S

    for i in range(len(S)):
        simqueue = simqueue[1:] + simqueue[0]
        if  simqueue < output:
            output = simqueue
    return output
    
S = eval(input())
print(func(S))
'''
#************
'''
def func(mylist):
    dict = {}
    for key in mylist:
        dict[key] = dict.get(key, 0) + 1
    lis = sorted(dict.keys())

    output = [dict[lis[0]]]
    for i in range(1,len(lis)):
        c = i - 1
        count = dict[lis[i]]
        while c >= 0 and lis[c] >= lis[i] - 10000:
            count += dict[lis[c]]
            c -= 1
        output.append(count)
    return output
    
mylist = eval(input())
print(func(mylist))


from pythonds.basic.queue import Queue
def hotPotato(namlist,num):
    simqueue = Queue()
    for name in namlist:
        simqueue.enqueue(name)#先排队；6个人这里的话，是从0号到5号
    
    while simqueue.size() > 1:
        for i in range(num-1):#这0到num-2个人保住了,合计num-1个人;num可以比namlist的size大
            simqueue.enqueue(simqueue.dequeue())
        print(simqueue.dequeue())#弹出标号为num-1的人，实际喊的是num，令其永不入队
    
    return simqueue.dequeue()#返回最后剩谁

print(hotPotato(["bill","david","susan","jane","kent","brad"],7))

'''

from pythonds.basic.deque import Deque
'''
class Deque:
    def __init__(self):
        self.items = []
    
    def addFront(self,item):#O(1)
        self.items.append(item)
    
    def removeFront(self):#O(1)
        return self.items.pop()

    def addRear(self,item):#O(n)
        self.items.insert(0,item)
    
    def removeRear(self):#O(n)
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
'''
def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        stillEqual = (first == last)
    return stillEqual

print(palchecker("lsdkjfskf"))