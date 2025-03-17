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