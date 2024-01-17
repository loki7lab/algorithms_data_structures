class Fraction:
    #定义方法
    def __init__(self,top,buttom):
        self.num = top
        self.den = buttom
        #self是一个总指向对象本身的特殊参数，必须是1st
        #要创建类，必须调用构造方法e.g.
        #myfraction = Fraction(3,5)
    def show(self):
        print(self.num,"/",self.den)
        #print(myfraction)是地址
        #print(myfraction.show)才是3/5
    #重写默认实现
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
        #myf = Fraction(3,5)
        #print(myf)成了3/5
        #myf.__str__()为'3/5'
        #str(myf)为'3/5'
    #**重写加法**
    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + \
                self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    #重写相等
    #只有在f1和f2是同一个对象的引用时，f1==f2才是True(浅相等)；值相等才是深相等
    def __eg__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum
#最简分数
def gcd(self,m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n