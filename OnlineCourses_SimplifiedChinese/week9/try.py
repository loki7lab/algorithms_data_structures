#***************binaryTree LIST**************
'''
def binaryTree(r):
    return [r,[],[]]
#print(binaryTree('c'))

def insertLeft(root,newBranch):
    t = root.pop(1)#poppde
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])#del left subtree,rebuild it as newBranch and insert back
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


r = binaryTree(3)
insertLeft(r,4)
print('all r :',r)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print("l :",l)
print("r :",r)
print('*****')
setRootVal(l,9)
print("r :",r)

insertLeft(l,11)
print('r :',r)

print(getRightChild(getRightChild(r)))
'''

#**************BINARYTREE node*********************

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild#update t with adding self.leftChild
            self.leftChild = t #replace self.leftchild with t
    
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self,obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    
    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

'''
r = BinaryTree('a')
print(r.getRootVal())
print('LeftChildVal: ',r.getLeftChild())
r.insertLeft('b')
print('leftChild :',r.getLeftChild())
print('LeftChildVal :',r.getLeftChild().getRootVal(),'type :',type(r.getLeftChild().getRootVal))#,r.getLeftChild().getRootVal():get LEAF value
r.insertRight('c')
r.getRightChild().setRootVal('hello')
print('RightChildVal :',r.getRightChild().getRootVal())
'''



#**************ParseTree********************
#from pythonds.trees import BinaryTree
from pythonds.basic.stack import Stack
#************build**************************

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    #eTree = BinaryTree('*')
    #print(eTree.getRootVal())#etree:*
    pStack.push(eTree)
    currentTree = eTree#currentTree works as Pointer item #进行引用传递，利用指针修改局部也是整体修改


    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            #currentTree.insertLeft('**')
            '''
            print(currentTree.getRootVal())#*
            print(currentTree.getLeftChild().getRootVal())#**
            print(eTree.getRootVal())#*
            print(eTree.getLeftChild().getRootVal())#**
            '''
            pStack.push(currentTree)#push the currentTree with new null sub-left-tree to save the whole tree
            '''
            print(type(pStack.peek()))#<class 'pythonds.trees.binaryTree.BinaryTree'>
            print(pStack.peek().getRootVal())#*
            print(pStack.peek().getLeftChild().getRootVal())#**
            pStack.pop()
            print(pStack.peek().getRootVal())#*
            print(pStack.peek().getLeftChild().getRootVal())#**
            pStack.pop()#pop the parent node
            #pStack.pop()#pop from empty list
            #in all，currentTree = eTree is passing by reference
            '''
            
            currentTree = currentTree.getLeftChild()#move to new null sub-left-tree or rather ,the new local / leaf
            #print(currentTree.getRootVal()) 

        elif i not in ['+','-','*','/',')']:
            currentTree.setRootVal(eval(i))#set the value of current (subtree's root node)/(leaf)
            parent = pStack.pop()#get parent tree,or rather the whole tree
            #print(parent.getLeftChild().getRootVal())#3
            #print(parent.getRootVal())#*
            currentTree = parent# move to the whole tree
            #print(currentTree.getRootVal())#*
            #print(currentTree.getLeftChild().getRootVal())#3

        elif i in ['+','-','*','/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)#save the whole tree
            currentTree = currentTree.getRightChild()#move to the local

        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError("unknown operator :" + i)
    return eTree



#buildParseTree('( 3 )')

#************evaluate***********

import operator
'''
def evaluate(ParseTree):
    opers = {'+':operator.add, '-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftC = ParseTree.getLeftChild()
    rightC = ParseTree.getRightChild()

    if leftC and rightC:
        fn = opers[ParseTree.getRootVal()]#it's awlways the operator character that is in root.
        #make it easy for +-*/
        return fn(evaluate(leftC),evaluate(rightC))

    else:
        return ParseTree.getRootVal()

ParseTree = buildParseTree('( ( 3 + 4 ) * 9 )')#notice!全括号，有空格
print(evaluate(ParseTree))
'''
#***********postordereval*****************
def postordereval(tree):
    opers = {'+':operator.add,'-':operator.sub,\
            '*':operator.mul,'/':operator.truediv}
    res1 = None
    res2 = None

    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()