from typing import List
from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchLeft(node: TreeNode, x: int):
    if node.val >= x:
        return False

    resultLeft = True
    resultRight = True

    if node.left != None: 
        resultLeft = searchLeft(node.left, x)

    if node.right != None: 
        resultRight = searchLeft(node.right, x)

    if resultLeft and resultRight:
        return True
    return False

def searchRight(node: TreeNode, x: int):
    if node.val <= x:
        return False

    resultLeft = True
    resultRight = True

    if node.left != None: 
        resultLeft = searchRight(node.left, x)

    if node.right != None: 
        resultRight = searchRight(node.right, x)

    if resultLeft and resultRight:
        return True
    return False

def isValidBST(root: Optional[TreeNode]) -> bool:
    if root.left == None and root.right == None:
        return True

    isLeftProper = False 
    isRightProper = False 

    if root.left != None:
        isLeftProper = searchLeft(root.left, root.val)
    else:
        isLeftProper = True

    if root.right != None:
        isRightProper = searchRight(root.right, root.val)
    else:
        isRightProper = True

    if isLeftProper and isRightProper:
        return True
    else:
        return False

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    d = defaultdict(set)  # O(1) lookup structure
    for x, y in edges:
        d[x].add(y)
        d[y].add(x)
        
    print(d)

    seen = set()

    def DFS(node):
        print(node)
        if node == destination:
            return True

        seen.add(node)
        print(seen)
        for n in d[node]:
            if n not in seen:
                return DFS(n)
        return False

    return DFS(source)

if __name__ == '__main__':
    
    result = validPath(10, [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]], 5, 9)
    print(result)

    result = validPath(10, [[2,6],[4,7],[1,2],[3,5],[7,9],[6,4],[9,8],[0,1],[3,0]], 3, 5)
    print(result)
    #root = TreeNode(32, TreeNode(26, TreeNode(19, None, TreeNode(27)), None), TreeNode(47, None, TreeNode(56)))  
    #print(isValidBST(root))