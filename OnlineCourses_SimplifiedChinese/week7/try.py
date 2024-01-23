#*****************sequentialSearch*****************
#not ordered
'''
def sequentialSearch(alist,item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found

testList = [1,2,32,8,17,19,42,13]
print(sequentialSearch(testList,3))
print(sequentialSearch(testList,13))

'''
#ordered
'''
def orderedSequentialSearch(alist,item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found

testlist = [0,1,2,8,13,17,19,32,42]
print(orderedSequentialSearch(testlist,3))
print(orderedSequentialSearch(testlist,13))
'''
#*************binarySearch********************
'''
def binarySearch(alist,item):
    found = False
    first = 0
    last = len(alist) - 1
    if first <= last and not found:
        mid = (first + last) // 2
        if alist[mid] == item:
            found = True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return found

testlist = [0,1,2,8,13,17,19,32,42]
print(binarySearch(testlist,3))
print(binarySearch(testlist,13))
'''
#recursive
'''
def recBinarySearch(alist,item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist)//2
        if alist[mid] == item:
            return True
    
    if alist[mid] < item:
        return recBinarySearch(alist[:mid],item)
    else:
        return recBinarySearch(alist[mid+1:],item)

testlist = [0,1,2,8,13,17,19,32,42]
print(recBinarySearch(testlist,3))
print(recBinarySearch(testlist,13))
'''
#****************bubbleSort******************
'''
def bubbleSort(alist):
    for passnum in range(len(alist) - 1,0,-1):#from n-1 to 1
        for i in range(passnum):#only do it in the useful area
            if alist[i] > alist[i + 1]:
                alist[i],alist[i + 1] = alist[i + 1],alist[i]
                #temp = alist[i]
                #alist[i] = alist[i + 1]
                #alist[i + 1] = temp
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
'''
#shortBubbleSort
'''
def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist) - 1
    while exchange and passnum > 0:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[1 + i]:
                exchange = True#ever changed and no longer be false
                alist[i],alist[i+1] = alist[i+1],alist[i]
        passnum -= 1
alist = [20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)
'''
#**********selectionSort**************
'''
def selectionSort(alist):
    for fillsolt in range(len(alist) - 1,0,-1):
        positionOfMax = 0
        for location in range(1,fillsolt + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        alist[fillsolt],alist[positionOfMax] = alist[positionOfMax],alist[fillsolt]

alist = [20,30,40,90,50,60,70,80,100,110]
selectionSort(alist)
print(alist)
'''
#****************InsertionSort*********************
'''
def InsertionSort(alist):
    for index in range(1,len(alist)):
        position = index
        currentValue = alist[index]
        
        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]#extra the last and other items move backward
            position -= 1
        
        #when find alist[position - 1] <= currentValue
        alist[position] = currentValue
alist = [20,30,40,90,50,60,70,80,100,110]
InsertionSort(alist)
print(alist)
'''
#********************shellSort***************************
'''
def shellSort(alist):
    sublistCount = len(alist)//2
    while sublistCount > 0:
        for startPosition in range(sublistCount):
            gapInsertionSort(alist,startPosition,sublistCount)
        print("After increments of size ",sublistCount,",this list is ",alist)
        sublistCount = sublistCount // 2

def gapInsertionSort(alist,startPosition,sublistCount):
    for i in range(startPosition + sublistCount,len(alist),sublistCount):#the first parameter must be the 2nd of sublist
        currentValue = alist[i]
        position = i
        while position >= sublistCount and alist[position - sublistCount] > currentValue:
            #position >= sublistCount to end this loop;position < sublistCount:alist[position] is the 1st of this sublist which have been done
            #alist[position - sublistCount] > currentValue:the prior > currentValue
            alist[position] = alist[position - sublistCount]#move backward
            position -= sublistCount
        alist[position] = currentValue

alist = [40,90,50,80,70]
shellSort(alist)
print(alist)
'''
#******************mergeSort***************************
'''
def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    
    mid = len(alist)//2
    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])

    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged

alist = [40,90,50]
lst = mergeSort(alist)#attention!
print(lst)
'''
#************************quickSort**************************
def quickSort(alist):
    quickSortHelper(alist,0,len(alist) - 1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint - 1)
        quickSortHelper(alist,splitpoint + 1,last)

def partition(alist,first,last):
    pivotValue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotValue:
            leftmark += 1
        while rightmark >=leftmark and alist[rightmark] >=pivotValue:
            rightmark -= 1
        # 209-212:make sure sublists are divided by whether every item of them > or < pivotValue
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
    
    alist[first],alist[rightmark] = alist[rightmark],alist[first]
    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)