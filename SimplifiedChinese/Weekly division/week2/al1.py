

def anagramSolution1(s1,s2):#逐字检查法，这个问题复杂度是O(n^2)
    alist = list(s2)#复制到列表中
    pos1 = 0
    stillOK = True
    while pos1 < len(s1) and stillOK:#循环s1中的每一个字符
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:#把s1中的每个字符都放进s2中对比
            if s1[pos1] == alist[pos2]:#对比成功
                found = True
            else:#对比失败就下一个
                pos2 += 1
        if found:#如果找到，就打勾
            alist[pos2] = None
        else:
            stillOK = False#没找到，就不是变位词
            break
        pos1 += 1
    return stillOK
print(anagramSolution1('abcd','dcab'))