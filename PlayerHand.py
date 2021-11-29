# PlayerHand
from Card import Card
class PlayerHand:

    def __init__(self):
        self.root = None
        self.size = 0

    def getTotalCards(self): # works
        return self.size

    def getMin(self): # works
        current = self.root
        #print("get min")
        while current.getLeft() is not None: # also can function as has left
            current = current.leftChild
        return current

    def getSuccessor(self, suit, rank):
        currentNode = self.get(suit, rank)
        succ = self.getSuccHelper(currentNode)
        return succ

    def getSuccHelper(self, currentNode):
        succ = None
        if currentNode.getRight():
            succ = currentNode.rightChild.getMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.getSuccessor()
                    self.parent.rightChild = self
        return succ

    def put(self, suit, rank): # seems to work but idk
        if self.root:
            self._put(suit, rank, self.root)
        else:
            self.root = Card(suit, rank)
        self.size += 1

    def _put(self, suit, rank, currentNode): # helper
        #print("Current Node:", currentNode, "Suit:", suit, "Rank:", rank)
        if rank < currentNode.rank:
            #print(1)
            if currentNode.getLeft():
                #print(2)
                self._put(suit, rank, currentNode.leftChild)
                #print(3)
            else:
                #print(4, currentNode)
                currentNode.leftChild = Card(suit, rank)
                #print(45, currentNode)
                self.parent = currentNode
                #print(5, currentNode)
        elif self.get(suit, rank):
            #print("count:", currentNode)
            node = self.get(suit, rank)
            count = 1
            node.setCount(count)
            
        else:
            #print(6)
            if currentNode.getRight():
                #print(7)
                self._put(suit, rank, currentNode.rightChild)
                #print(8)
            else:
                #print(9)
                currentNode.rightChild = Card(suit, rank)
                self.parent = currentNode
                

    def delete(self, suit, rank): # doesn't work
        yOrN = False
        if self.size > 1:
            nodeToRemove = self._get(suit, rank, self.root)
            #print(2, nodeToRemove)
            if nodeToRemove and (nodeToRemove.count > 1):
                #print(3, nodeToRemove)
                self.size -= 1
                nodeToRemove.count -= 1
                yOrN = True
                return yOrN
            elif nodeToRemove:
                #print(4, nodeToRemove)
                self.remove(nodeToRemove)
                self.size -= 1
                yOrN = True
                return yOrN
            else:
                return yOrN
        elif self.size == 1 and self.root.rank == rank:
            #print(5, nodeToRemove)
            self.root = None
            self.size -= 1
            yOrN = True
            return yOrN
        else:
            return yOrN

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.getSuccessor(currentNode.suit, currentNode.rank)
            succ.spliceOut()
            currentNode.suit = succ.suit
            currentNode.rank = succ.rank
        else:
            if currentNode.getLeft():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.suit,
                                                currentNode.leftChild.rank,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.suit,
                                                currentNode.rightChild.rank,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

    def isEmpty(self): # works
        return self.size == 0 # return boolean value

    def get(self, suit, rank): # works
        if self.root:
            res = self._get(suit, rank, self.root)
            if res:
                return res # wrong dont know what should be here
            else:
                return None
        else:
            return None

    def _get(self, suit, rank, currentNode):
        if not currentNode:
            return None
        elif currentNode.rank == rank and currentNode.suit == suit:
            return currentNode
        elif rank < currentNode.rank:
            return self._get(suit, rank, currentNode.leftChild)
        else:
            return self._get(suit, rank, currentNode.rightChild)

    def inOrder(self):
        order = self.orderHelper(self.root)
        return order

    def orderHelper(self, node): # works
        string = ""
        if node != None:
            #print("Before node.leftchild:", 0, string)
            string += self.orderHelper(node.leftChild)
            #print("Before node.rank:", 1, string)
            string += str(node)
            #print("Before right.child:", 2, string)
            string += self.orderHelper(node.rightChild)
            #print("After right.child", 3, string)
        return string
            

    def preOrder(self): # works
        preOrder = self.preOrderHelper(self.root)
        return preOrder

    def preOrderHelper(self, node):
        string = ""
        if node != None:
            #print(1)
            string += str(node)
            #print(2)
            string += self.orderHelper(node.leftChild)
            #print(3)
            string += self.orderHelper(node.rightChild)
        return string

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChildren():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightCHild
                self.rightChild.parent = self.parent
