class Node:
    def __init__(self,initData):
        self.data = initData
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newData):
        self.data = newData
    def setNext(self,newNext):
        self.next = newNext


class OrderedList:
    
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.getData()))
            current = current.getNext()
        return (" -> ".join(elements))

#变动在这里
    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:#非空再判断下一步，不用getData()
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True#比无序表有变动！
                else:
                    current = current.getNext()
        return found
    
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        #找位置
        while current != None and not stop:#这里就俩
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)

        temp.setNext(current)
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)
'''

        #新项在开头
        
        if previous == None:
            temp.setNext(self.head)#或者用self.head；这里current就是最开始的
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
'''   

# 测试用例

ol = OrderedList()

ol.add(31)

ol.add(77)

ol.add(17)

ol.add(93)

ol.add(6)

ol.add(54)


print(ol.size())# == 6), "size 方法测试失败：列表元素数量应为 6"


print(ol.display())