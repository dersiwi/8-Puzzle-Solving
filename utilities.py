from queue import PriorityQueue
from random import randrange 


def getRandomBoard():
    return [[7, 2, 4], [5, 0, 6], [8, 3, 1]]

def doXRandomMoves(startConfig, x):
    
    b = getCopy(startConfig)

    for i in range(x):
        legalMoves = getLegalMoves(b)
        move = legalMoves[randrange(len(legalMoves))]
        doMove(b, move)
    return b

def doMove(board, move):
    board[move[1][0]][move[1][1]] = board[move[0][0]][move[0][1]]
    board[move[0][0]][move[0][1]] = 0

def printBoard(board):
    boardString = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                boardString += " "
            else:
                boardString += str(board[i][j])
            if j < 2:
                boardString += " | "
        if i < 2:
            boardString += "\n---------\n"
    print(boardString)

"""
Returns a list of lists like so;
[
    [(i, j), (i', j')]
]
Which means, a move from i, j to i', j' is posible.
"""
def getLegalMoves(board):
    legalMoves = []
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == 0):
                
                if i - 1 >= 0:
                    legalMoves.append([
                        (i-1, j), (i, j)
                    ])
                if i + 1 < 3:
                    legalMoves.append([
                        (i+1, j), (i, j)
                    ])
                if j - 1 >= 0:
                    legalMoves.append([
                        (i, j-1), (i, j)
                    ])
                if j + 1 < 3:
                    legalMoves.append([
                        (i, j+1), (i, j)
                    ])
    return legalMoves






#-----------------------------------------------------------Implementing the algorithm---------------------------

"""
A data structure is needed, which stores the distance to each node, the so-called "fringe".
"""


class PrioQueue:
    def __init__(self):
        self.q = PriorityQueue()
        self.inserted = ClosedQueue()

    
    def insert(self, prio, board):
        key = ClosedQueue.getKey(board)

        if self.inserted.contains(key):
            return
        self.q.put(
            (prio, board)
        )
        self.inserted.insert(key)

    def getMin(self):
        return self.q.get()
    
    def empty(self):
        return self.q.empty()

class ClosedQueue:
    def __init__(self):
        self.closed = []

    """
    basically a hash-function for boards, by mapping each board onto a unique string
    -> probably slow
    """
    def getKey(board):
        k = ""
        for i in range(len(board)):
            for j in range(len(board[i])):
                k += str(board[i][j])
        return k

    def contains(self, board):
        key = ClosedQueue.getKey(board)
        for k in self.closed:
            if key == k:
                return True
        return False

    def insert(self, board):
        self.closed.append(ClosedQueue.getKey(board))

class SearchTreeNode():
    def __init__(self, board):
        self.board = board
        self.parent = None
        self.depth = None
    
    def setParent(self, parentNode):
        self.parent = parentNode

    def getParent(self):
        return self.parent
    
    def getBoard(self):
        return self.board
    
    def getListToParent(self):
        nodeList = []
        node = self
        while node != None:
            nodeList.insert(0, node)
            node = node.getParent()
        return nodeList

    def getDepth(self):
        if self.depth == None:
            if self.parent != None:
                self.depth = 1 + self.parent.getDepth()
            else:
                self.depth = 0
        return self.depth

class SearchTree():
    def __init__(self):
        self.treeNodes = {}
    
    def insert(self, board):
        key = ClosedQueue.getKey(board)
        self.treeNodes[key] = SearchTreeNode(board)
        return self.treeNodes[key]

    
    def getTreeNode(self, board):
        return self.treeNodes[ClosedQueue.getKey(board)]

    def getAmountNodes(self):
        return len(self.treeNodes)


"""
check if board equals the following array:
[
    [0,1,2],
    [3,4,5],
    [6,7,8]
]
"""
def isSolved(board):
    for i in range(len(board)):
        for j in range(len(board)):
            
            if board[i][j] != i*3 +j:
                return False 
    return True


def getCopy(board):
    copy = []
    for i in range(len(board)):
        copy.append([])
        for j in range(len(board[i])):
            copy[i].append(board[i][j])
    return copy

