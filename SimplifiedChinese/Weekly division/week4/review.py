
class Node:#生成节点
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:#基于节点集合来构建
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self,item):
        tem = Node(item)
        tem.setNext(self.head)
        self.head = tem
    def length(self):
        current = self.head#通用计数器而不是个体的
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    def search(self,item):
        current = self.head
        found = False
        while current.getData != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext
        return found
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:#0号位节点被移除
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

class OrderedList:
    def __init__(self):
        self.head = None
    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        tem = Node(item)
        if previous == None:
            tem.setNext(self.head)
            self.head = tem
        else:
            tem.setNext(current)
            previous.setNext(tem)