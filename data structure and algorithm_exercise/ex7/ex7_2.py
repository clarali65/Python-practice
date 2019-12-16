lst = list(input().split())
lst = [0] + lst
for i in range(2, len(lst)):  # 将lst正则化，即转换成‘完全二叉树’式的非嵌套列表，使None的子节点都是None
    if lst[i // 2] == None:  # 如果这个元素的父节点是None,那么这个元素不能连在这里，所以把它右移
        if i == len(lst) - 1:  # 分两种情况，如果是最后一个元素的话，那么他右移要超出list的下标了，所以list先扩充一格
            lst = lst + [None]  # lst加一格
            lst.insert(i + 2, lst[i])  # 将此时的元素插入到后两格的位置
            lst[i] = None  # 然后把原来的位置变成None
        else:  # 如果不是最后一个元素的话，直接在后两格的位置insert就行
            lst.insert(i + 2, lst[i])
            lst[i] = None
# 递归实现中序遍历
result = []

def inorderTree(root):  # (root是根节点的下标)
    if root * 2 <= len(lst) - 1:  # 如果有左子树的话
        inorderTree(root * 2)  # 遍历左子树
    if lst[root] != None:  # 将根节点保存到result列表中(如果不是None的话)
        result.append(lst[root])
    if root * 2 + 1 <= len(lst) - 1:  # 如果有右子树的话
        inorderTree(root * 2 + 1)  # 遍历右子树


inorderTree(1)
print(' '.join(str(x) for x in result[::-1]))