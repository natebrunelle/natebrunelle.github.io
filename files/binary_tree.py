import binary_strings.py

def makeEmptyTree():
    """Returns the empty tree."""
    return "*"
    
def isEmpty(t):
    """Takes a Tree as input, and outputs a Boolean indicating if the input is an empty tree"""
    return t == "*"

def mergeTrees(l, r):
    """Takes two Trees as inputs, and outputs a Tree whose left branch is the first input, and whose right branch is the second input."""
    return (l,r)
    
def getLeftBranch(t):
    """Takes a non-empty Tree as input, and outputs the left branch of that Tree. (Note that this is a partial function. It is not defined for the empty tree, and fails with an error on that input.)"""
    assert(not isEmpty(t))
    return t[0]

def getRightBranch(t):
    """Takes a non-empty Tree as input, and outputs the right branch of that Tree. (Note that this is a partial function. It is not defined for the empty tree, and fails with an error on that input.)"""
    assert(not isEmpty(t))
    return t[1]

emptyTree = makeEmptyTree()
print(emptyTree)

fullHeight1 = mergeTrees(emptyTree, emptyTree)
print(fullHeight1)

fullHeight2 = mergeTrees(fullHeight1, fullHeight1)
print(fullHeight2)

fullHeight3 = mergeTrees(fullHeight2, fullHeight2)
print(fullHeight3)

unbalancedHeight4 = mergeTrees(fullHeight1, fullHeight3)
print(unbalancedHeight4)


"""TODO: Define 'treeSize' and 'treeHeight' functions which take a single Tree as their input, and output an int that represents the total number of nodes in the tree andthe height of the tree respectively. """

def treeSize(t):
    """takes a tree as input, gives the number of nodes in the tree as output"""
    if isEmpty(t):
        return 0
    else:
        left = getLeftBranch(t)
        right = getRightBranch(t)
        return treeSize(left) + treeSize(right)
    return -1


def treeHeight(t):
    """takes a tree as input, gives the height of the tree as output"""
    if isEmpty(t):
        return 0
    else:
        left = getLeftBranch(t)
        right = getRightBranch(t)
        return max(treeHeight(left), treeHeight(right))
    return -1
    
# Some tests for treeeSize
assert(treeSize(emptyTree) == 0)
assert(treeSize(fullHeight1) == 1)
assert(treeSize(fullHeight2) == 3)
assert(treeSize(fullHeight3) == 7)
assert(treeSize(unbalancedHeight4) == 9)

# Some tests for treeeHeight
assert(treeHeight(emptyTree) == 0)
assert(treeHeight(fullHeight1) == 1)
assert(treeHeight(fullHeight2) == 2)
assert(treeHeight(fullHeight3) == 3)
assert(treeHeight(unbalancedHeight4) == 4)
