class BinTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.leftfuck = 0
        self.rightfuck = 0

def seq2tree(seq):
    queue = []
    i = 1
    currentTree = BinTree(seq[0])
    finaltree = currentTree
    queue.append(currentTree)
    while i < len(seq) and len(queue) > 0:
        currentTree = queue.pop(0)
        if seq[i] == None:
            if currentTree.leftfuck == 0 and currentTree.rightfuck == 0:
                currentTree.leftfuck = 1
                queue.insert(0, currentTree)
            elif currentTree.leftfuck == 1 and currentTree.rightfuck == 0:
                currentTree.rightfuck = 1
            i = i + 1

        else:
            if currentTree.leftfuck == 0 and currentTree.rightfuck == 0:
                currentTree.leftfuck = 1
                currentTree.left = BinTree(seq[i])
                queue.append(currentTree.left)
                queue.insert(0, currentTree)
                i = i+1
            elif currentTree.leftfuck == 1 and currentTree.rightfuck == 0:
                currentTree.rightfuck = 1
                currentTree.right = BinTree(seq[i])
                queue.append(currentTree.right)
                i = i + 1
            else:
                i = i
    return finaltree

def inorderTree(root):
    if root == None:
        return []
    else:
        left = inorderTree(root.left)
        data = root.data
        right = inorderTree(root.right)
        return left + [data] + right

lst = eval(input())
tree = seq2tree(lst)
inorder = inorderTree(tree)
print(' '.join(str(x) for x in inorder))