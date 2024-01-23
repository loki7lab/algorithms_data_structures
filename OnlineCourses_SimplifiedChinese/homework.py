#*****************1****************
def seq2tree(seq):
    def BinTree(r):
        return [r, [], []]

    finalTree = BinTree(seq[0])
    queue = [finalTree]
    for num in seq[1:]:
        currentTree = queue.pop(0)
        if num == None:
            if currentTree[1] == []:
                currentTree[1].append(num)
                queue.insert(0, currentTree)
            else:
                currentTree[2].append(num)
        else:
            if currentTree[1] == []:
                currentTree[1] = BinTree(num)
                queue.insert(0, currentTree)
                queue.append(currentTree[1])
            else:
                currentTree[2] = BinTree(num)
                queue.append(currentTree[2])
    return finalTree


def inorderTree(tree):
    if tree == [] or tree == [None]:
        return []
    else:
        left = inorderTree(tree[1])
        root = tree[0]
        right = inorderTree(tree[2])
        return left + [root] + right


lst = eval(input())
tree = seq2tree(lst)
inorder = inorderTree(tree)
print(*inorder)

#***************************2*************************
def inorder(root):
    if root * 2 + 1 <= len(lst) - 1:
        inorder(root * 2 + 1)
    result.append(lst[root])
    if root * 2 <= len(lst) - 1:
        inorder(root * 2)


lst = list(input().split())
lst = ['0'] + lst
result = []
inorder(1)
print(*result)
#***********************3**********************
def postorderTree(tree):
    if len(tree) == 1:
        return tree
    else:
        result = []
        for i in range(1, len(tree)):
            result += postorderTree(tree[i])
        result += [tree[0]]
        return result


lst = eval(input())
postorder = postorderTree(lst)
print(*postorder)
