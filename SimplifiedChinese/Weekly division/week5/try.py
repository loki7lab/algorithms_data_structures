#********任意进制转换********
'''
def toStr(n,base):
    convertString = "012345678910ABCDEF"
    if base > n:
        return convertString[n]
    else:#use string not number to make sure that it doesnt be add in decimal base 
        a = toStr(n//base,base)#woc 666
        b = convertString[n%base]
        return a+b

print(toStr(4,2))

'''

#*********turtle plot**************
'''
import turtle

t = turtle.Turtle()

def drawSpiral(t,lineLen):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t,lineLen - 5)
drawSpiral(t,100)
turtle.done()
'''

#************tree****************
'''
import turtle

def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15)
        t.left(40)
        tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)#attention there is always the EndPlot where no matter turn left/right/backward
        #on the endplot,it always return back to the fork point and turn left

t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)#不留痕迹退回100步
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(75)
t.hideturtle()
turtle.done()
'''

#******sierpinski triangle**************

'''
import turtle

def sierpinski(degree,points):
    colormap = ['blue','red','green','white','yellow','orange']
    drawTriangle(points,colormap[degree])
    if degree > 0:
        sierpinski(degree - 1,
                    {'left':points['left'],
                    'top':getMid(points['top'],points['left']),
                    'right':getMid(points['left'],points['right'])
                    })
        sierpinski(degree - 1,
                    {'left':getMid(points['left'],points['top']),
                    'top':points['top'],
                    'right':getMid(points['top'],points['right'])}
                    )
        sierpinski(degree - 1,
                    {'left':getMid(points['left'],points['right']),
                    'top':getMid(points['top'],points['right']),
                    'right':points['right']})

def drawTriangle(points,color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

def getMid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

t = turtle.Turtle()
points = {'left':(-200,-100),
            'top':(0,200),
            'right':(200,-100)}

sierpinski(3,points)
turtle.done()
'''
#*************hanoi*******************
'''
def moveTower(height,fromPole,withPole,toPole):
    if height >= 1:
        moveTower(height - 1,fromPole,toPole,withPole)
        moveDisk(height,fromPole,toPole)
        moveTower(height - 1,withPole,fromPole,toPole)
def moveDisk(disk,fromPole,toPole):
    print(f"Moving disk[{disk}] from {fromPole} to {toPole} ")

moveTower(5,"1#","2#","3#")
'''
#**********Maze*******************
'''
class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName,'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)
'''
#***************括号匹配*********************
def match(s, n=0):
    if s:
        if s[0] == '(':
            n += 1
        else:
            n -= 1
            if n < 0:
                return False
        return match(s[1:], n)
    else:
        return n == 0