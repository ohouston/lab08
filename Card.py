### Card.py
# tree node?
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.count = 1

    def getSuit(self):
        return self.suit

    def setSuit(self, suit):
        self.suit = suit
        return suit

    def getRank(self):
        return self.rank

    def setRank(self, rank):
        self.rank = rank
        return self.rank

    def getCount(self): # what is the count for
        return self.count

    def setCount(self, count): # redo this one
        self.count += count
        return self.count

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent
        return self.parent

    def getLeft(self): # hasLeft
        return self.leftChild

    def setLeft(self, left):
        self.leftChild = left
        return self.leftChild

    def getRight(self): # hasRight
        return self.rightChild

    def setRight(self, right):
        self.rightChild = right
        return self.rightChild

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not(self.rightChild or self.leftChild)

    def isLeftChild(self):
        return self.parent and \
               self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and \
               self.parent.rightChild == self

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, suit, rank, lc, rc):
        self.suit = suit
        self.rank = rank
        self.leftChild = lc
        self.rightChild = rc
        if self.getLeft():
            self.leftChild.parent = self
        if self.getRight():
            self.rightChild.parent = self

    def helper_put(self, suit, rank, parent):
        self.suit = suit
        self.rank = rank
        self.parent = parent

    def __str__(self):
        return "{} {} | {}\n".format(self.suit.upper(), self.rank.upper(), self.count)
'''
#optional but not at the same
    def __gt__(self, other):
            return

    def __lt__(self, other):
        if self.rank.upper() == 'A':
            return int(self.rank.upper()) < other.rank.upper()

    def __int__(self):
        if self.rank.upper() == 'A':
            return 1

# makes my other stuff not work...

    #def __eq__(self, other):
       # return self.rank.upper() == other.rank.upper()
    
'''















        
