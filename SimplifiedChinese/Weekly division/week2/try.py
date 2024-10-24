'''
l1 = list(range(1000))#fastest

l2 = [i for i in range(1000)]

l3 = []
for i in range(1000):
    l3.append(i)

l4 = []#slowest
for i in range(1000):
    l4 += [i] 

for i in range (10000,1000001,20000):#start,end,step
    x = {j:None for j in range(i) }
for key,value in x.items():
    print((key,value))
'''
from timeit import Timer


def test4():
    l = list(range(1000))

t4 = Timer("test4()","from __main__ import test4")
#Object Timer:1st par---the sentences to repeat.
#2nd par --- setup sentence where the pars need to import 
#from __main__ import:main namespace
print("list range %f seconds\n"%t4.timeit(number=1000))
