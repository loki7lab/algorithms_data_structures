#*********************1**********************
class TreeNode:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.val = None
        self.leftChild = left
        self.rightChild = right


def generateTree(total):
    node_list = [TreeNode(i) for i in range(total)]
    for currentNode in node_list:
        seq = [int(j) for j in input().split()]
        if seq[0] != -1:
            currentNode.leftChild = node_list[seq[0]]
        if seq[1] != -1:
            currentNode.rightChild = node_list[seq[1]]

    return node_list[0]


def fillTree(root):
    if root:
        fillTree(root.leftChild)
        root.val = lst.pop(0)
        fillTree(root.rightChild)


def printTree(total):
    queue = [root]
    result = []
    for i in range(total):
        currentNode = queue.pop(0)
        result.append(currentNode.val)
        if currentNode.leftChild:
            queue.append(currentNode.leftChild)
        if currentNode.rightChild:
            queue.append(currentNode.rightChild)
    print(*result)


N = int(input())
root = generateTree(N)
lst = [int(i) for i in input().split()]
lst.sort()
fillTree(root)
printTree(N)

#*****************2***********************
class TreeNode:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.val = None
        self.leftChild = left
        self.rightChild = right
        self.parent = parent


def generateTree(total):
    root = TreeNode(1)
    queue = [root]
    count = 1
    while count < total:
        currentNode = queue.pop(0)
        if count + 1 < total:
            count += 1
            currentNode.leftChild = TreeNode(count, parent=currentNode)
            queue.append(currentNode.leftChild)
            count += 1
            currentNode.rightChild = TreeNode(count, parent=currentNode)
            queue.append(currentNode.rightChild)
        else:
            count += 1
            currentNode.leftChild = TreeNode(count, parent=currentNode)
    return root


def fillTree(root):
    if root:
        fillTree(root.leftChild)
        root.val = lst.pop(0)
        fillTree(root.rightChild)


def printTree(total):
    queue = [root]
    result = []
    for i in range(total):
        currentNode = queue.pop(0)
        result.append(currentNode.val)
        if currentNode.leftChild:
            queue.append(currentNode.leftChild)
        if currentNode.rightChild:
            queue.append(currentNode.rightChild)
    print(*result)


lst = [int(num) for num in input().split()]
lst.sort()
N = len(lst)
root = generateTree(N)
fillTree(root)
printTree(N)

#****************************3**********************
class TreeNode:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.val = None
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def put(self, key):
        if key < self.key:
            if self.leftChild:
                self.leftChild.put(key)
            else:
                self.leftChild = TreeNode(key, parent=self)
        else:
            if self.rightChild:
                self.rightChild.put(key)
            else:
                self.rightChild = TreeNode(key, parent=self)


def generateTree():
    root = TreeNode(lst[0])
    for i in lst[1:]:
        root.put(i)
    return root


def changeTree():
    queue = [root]
    result = []
    for i in range(len(lst)):
        currentNode = queue.pop(0)
        total = 0
        for num in lst:
            if num >= currentNode.key:
                total += num
        result.append(total)
        if currentNode.leftChild:
            queue.append(currentNode.leftChild)
        if currentNode.rightChild:
            queue.append(currentNode.rightChild)
    print(*result)


lst = [int(num) for num in input().split()]
root = generateTree()
changeTree()
