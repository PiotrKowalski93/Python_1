from ast import List, operator
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def removeDuplicates(nums: List) -> int:
    if len(nums) == 1:
        return 1
    if len(nums) == 0 or nums == None:
        return 0

    endPtr = len(nums) - 1
    beginPtr = 0
    while beginPtr < endPtr:
        print("Begin: ", beginPtr, "| EndPtr: ", endPtr)
        if nums[beginPtr] == nums[beginPtr + 1]:
            nums.pop(beginPtr+1)
            nums.append(0)
            endPtr -= 1
        else:
            beginPtr += 1
    return beginPtr

def removeElement(nums: List, val: int) -> int:

        nums[:] = [ x for x in nums if x != val ]
        return len(nums)

        if len(nums) == 0:
            return 0

        beginPtr = 0
        endPtr = len(nums) - 1

        while beginPtr < endPtr:
            if nums[beginPtr] == val:
                nums.pop(beginPtr)
                nums.append(0)
                endPtr -= 1
            else:
                beginPtr += 1

        return endPtr + 1


def plusOne(digits: List) -> List:
        i = len(digits)
        while True:
            i -= 1
            if i == 0:
                digits[i] = 0
                digits[:] = [1] + digits
            digits[i] += 1
            if digits[i] > 9:
                digits[i] = 0
                continue
            else:
                break
        return digits

def isIsomorphic(s: str, t: str) -> bool:
        mapping = dict()
        mapped = set()
        for i in range(0, len(s)):
            m = mapping.get(s[i])
            if m == None:
                if t[i] in mapped:
                    return False
                else:
                    mapping[s[i]] = t[i]
                    mapped.add(t[i])
            else:
                  if m != t[i]:
                    return False      
        return True

def getHint(secret: str, guess: str) -> str:
    secretList = list(secret)
    guessList = list(guess)
    bulls = 0
    
    # Count Bulls
    for i in range(0, len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
            secretList.remove(secret[i])
            guessList.remove(guess[i])

    # Count Caws    
    guessLeft = ''.join(guessList)

    cows = 0
    for i in range(0, len(guessLeft)):
        if guessLeft[i] in secretList:
            cows += 1
            secretList.remove(guessLeft[i])

    result = str(bulls) + "A" + str(cows) + "B" 
    return result

def getHint(self, secret, guess):
    bulls = sum(map(operator.eq, secret, guess))
    both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
    return '%dA%dB' % (bulls, both - bulls)

def backspaceCompare(s: str, t: str) -> bool:
    sliced = True
    while sliced == True:
        sliced = False
        x = s.find("#")
        y = t.find("#")
        if x != -1:
            if x == 0:
                s = s[1:]
                sliced = True
            else:
                s = s[0:x-1] + s[x+1:]
                sliced = True
        if y != -1:
            if y == 0:
                t = t[1:]
                sliced = True
            else:
                t = t[0:y-1] + t[y+1:]
                sliced = True

    print(s, " ", t)
    if s == t: 
        return True
    return False

def inorderTraversal(root: TreeNode):
    if root == None:
        return List()
    if root.left == None and root.right == None:
        return [root.val]

    valuse = []

    def DFS(node: TreeNode):
        if node.left == None and node.right == None:
            valuse.append(node.val)

        if node.left != None:
            DFS(node.left)
        if node.right != None:
            DFS(node.right)

def singleNumber(nums) -> int:
    print(nums)
    if len(nums) == 1 or nums[0] != nums[1]:
        return nums[0]

    nums.sort()

    for i in range(1, len(nums) - 1):
        if nums[i-1] != nums[i] and nums[i+1] != nums[i]:
            return nums[i]

def containsNearbyDuplicate(nums: List, k: int) -> bool:       
        dict = {}

        for i in range(0, len(nums)):
            if nums[i] in dict:
                j = dict[nums[i]]
                if abs(i - j) <= k:
                    return True
            else:
                dict[nums[i]] = i
        return False

if __name__ == '__main__':

    containsNearbyDuplicate([1,0,1,1],1)

    #print(singleNumber([1,2,2]))

    #backspaceCompare("ab#c","ad#c")
    #backspaceCompare("ab##", "c#d#")
    #backspaceCompare("a#c", "b")
    #backspaceCompare("a##c", "#a#c")

    # print(getHint("1807","7810"))   # "1A3B"
    # print(getHint("1123","0111"))   # "1A1B"
    # print(getHint("11","10"))       # "1A0B"
    # print(getHint("1122","1222"))

    # print(isIsomorphic("egg", "add"))
    # print(isIsomorphic("foo", "bar"))
    # print(isIsomorphic("paper", "title"))
    # print(isIsomorphic("badc", "baba"))
        