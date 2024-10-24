'''
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: 
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False 
        return len(stack) == 1

#作者：jyd
#链接：https://leetcode-cn.com/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
#2.***********进制转换**************
'''
from pythonds.basic.stack import Stack
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()
    while decNumber > 0:
        decNumber = decNumber // base
        rem = decNumber % base
        remstack.push(rem)

    newString = ""
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]
    return newString

print(baseConverter(16,2))
'''
#************3.后序表达式*****************
'''
from pythonds.basic.stack import Stack
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "01234546789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMat(token,operand1,operand2)
            operandStack.push(result)
    
    return operandStack.pop()

def doMat(op,op1,op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2
'''
#************
class Stack:
    def __init__(self):#attention list&items
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):#attention return
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items == []# attention list
    def size(self):
        return len(self.items)
'''
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while balanced and index < len(symbolString):
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

print(parChecker('()'))
'''
#***16进制转换***
'''
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    
    newString = ''
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
    
    return newString
print(baseConverter(7,2))
'''
# 表达式转换
'''
def infixToPostfix(infixexpr):
    prec = {"*":3,"/":3,"-":2,"+":2,"(":1,}
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix(" ( A * B ) + C"))
'''
#*-*-***homework2*****
'''
def xiaoxiaole(Newstring):
    c = Stack()
    c.push('?')
    for i in Newstring:
        if i != c.peek():
            c.push(i)
        else:
            c.pop()
    if c.size() == 1:
        return None
    else:
        clist = []
        for m in range(1,c.size()):
            clist.append(c.pop())
        return clist


Newstring = input()
clists = xiaoxiaole(Newstring)
clists = clists[::-1]
print("".join(clists))
'''
#*****************OCDBoss*******************
def OCDBoss(NewString):
    leftList = []
    popList = []
    for i in NewString:
        i = int(i)
        for j in range(i+1):
            if j not in popList:
                if j not in leftList:
                    leftList.append(j)
            if leftList != []:
                if i == leftList[-1]:
                    popList.append(leftList.pop())
    #print(len(leftList))
    if len(leftList) > 0:
        print('No')
    else:
        print('Yes')
NewString = input()
OCDBoss(NewString)
