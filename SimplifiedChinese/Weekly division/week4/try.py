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

from pythonds.basic.queue import Queue
import random

#打印机类
class Print:
    def __init__(self,ppm):
        self.pageRate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:#不能用while,不然在这里就把任务干完了，没模拟时间流逝
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    
    def startNext(self,newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages()*60/self.pageRate#可以直接让任务为秒流逝吗

#任务本身情况
class Task:
    def __init__(self,time):
        #生成时间戳
        self.timestamp = time
        #生成打印页数
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self,currentTime):
        return currentTime - self.getStamp()

#触发任务的概率
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

#开启模拟
def simulation(numSeconds,pagesPerMinute):
    labPrinter = Print(pagesPerMinute)
    printQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if not labPrinter.busy() and not printQueue.isEmpty():
            nextTask = printQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            labPrinter.startNext(nextTask)
        labPrinter.tick()

    averageWait = sum(waitingTimes)/len(waitingTimes)
    print("average wait %6.2f secs %3d tasks remaining." %(averageWait,printQueue.size()))


for i in range(10):
    simulation(3600,5)