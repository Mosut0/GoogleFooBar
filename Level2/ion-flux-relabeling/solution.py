class Node:
    def __init__(self, root=None) -> None:
        self.root = root
        self.left = None
        self.right = None

def solution(h, q):
    elements = []
    for i in range(1, 2 ** h):
        elements.append(i)
    tree = postorder(h, elements)
    ans = [-1] * len(q)

    def findParent(head, node, parent, i):
        if (head is None):
            return
        if (head.root == node):       
            ans[i] = parent
        else:
            findParent(head.left, node, head.root, i)
            findParent(head.right, node, head.root, i)

    for i in range(len(q)):
        findParent(tree, q[i], -1, i)
    return ans

def postorder(height, nums):
    if height == 1:
        return Node(nums.pop())
    node = Node()
    node.root = nums.pop()
    node.right = postorder(height-1, nums)
    node.left = postorder(height-1, nums)
    return node

print(solution(5, [19, 14, 28]))
print(solution(3, [7, 3, 5, 1]))