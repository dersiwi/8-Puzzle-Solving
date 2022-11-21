import math
from queue import PriorityQueue
import time
from random import randrange 

#board = [[], [], []]


FINAL_POSITIONS = [[2,2]]
def getFinalPositions():
    global FINAL_POSITIONS
    for i in range(8):
        FINAL_POSITIONS.append([int((i) / 3), (i) % 3])
getFinalPositions()


def getRandomBoard():
    return [[7, 2, 4], [5, 0, 6], [8, 3, 1]]

def doXRandomMoves(x):
    
    b = [[1,2,3], [4,5,6], [7,8,0]]

    for i in range(x):
        legalMoves = getLegalMoves(b)
        move = legalMoves[randrange(len(legalMoves))]
        b[move[1][0]][move[1][1]] = b[move[0][0]][move[0][1]]
        b[move[0][0]][move[0][1]] = 0
    return b

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


def accManhattenDistance(board):
    amd = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                continue
            amd += manhattenDistance(board[i][j], i, j)
    return amd

"""
Cacculate the manhattenDistance of a number n on the board
"""
def manhattenDistance(n, currentI, currentJ):
    return int(math.ceil(
        math.sqrt(
            math.pow(currentI - FINAL_POSITIONS[n][0], 2) + 
            math.pow(currentJ - FINAL_POSITIONS[n][1], 2)
        )
    ))



#-----------------------------------------------------------Implementing the algorithm---------------------------

"""
A data structure is needed, which stores the distance to each node, the so-called "fringe".
"""


class PrioQueue:
    def __init__(self):
        self.q = PriorityQueue()
        self.inserted = ClosedQueue()

    def insert(self, board):
        key = ClosedQueue.getKey(board)

        if self.inserted.contains(key):
            return

        md = accManhattenDistance(board)
        self.q.put(
            (md, board)
        )
        self.inserted.insert(key)
    
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
solved = [[1,2,3],
    [4,5,6],
    [7,8,0]]

def isSolved(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != solved[i][j]:
                return False 
    return True


def getCopy(board):
    copy = []
    for i in range(len(board)):
        copy.append([])
        for j in range(len(board[i])):
            copy[i].append(board[i][j])
    return copy

searchTree = SearchTree()

def findSolution(board):

    
    papaNode = searchTree.insert(board)

    openQueue = PrioQueue()
    closedQueue = ClosedQueue()
    openQueue.insert(papaNode.getDepth() + accManhattenDistance(board), board)
    counter = 0
    while not openQueue.empty():
        counter += 1
        current_board = openQueue.getMin()[1] #get the board with min eval
        current_tree_node = searchTree.getTreeNode(current_board)

        if isSolved(current_board):
            return current_tree_node 

        #get all the possible boards, reachable from the current board and insert them into queue
        for move in getLegalMoves(current_board):
            bn = getCopy(current_board)
            bn[move[1][0]][move[1][1]] = bn[move[0][0]][move[0][1]]
            bn[move[0][0]][move[0][1]] = 0
            if not closedQueue.contains(bn):

                node = searchTree.insert(bn)
                node.setParent(current_tree_node)

                openQueue.insert(node.getDepth() + accManhattenDistance(bn), bn)
        closedQueue.insert(current_board)




def main():
    start_time = time.time()


    #solutionNode = findSolution(boardToSolve)
    #print(isSolved(doXRandomMoves(0)))
    solutionNode = findSolution(getRandomBoard())
    listToParent = solutionNode.getListToParent()

    print("Amout moves to solve : {}".format(len(listToParent) - 1))

    print("Total Explored Nodes : {}".format(searchTree.getAmountNodes()))
    


    print("--- %s seconds ---" % (time.time() - start_time))
    print("\n\n\n")

    answer = input("Print moves to solution?[Y/N]")
    if answer == "y" or answer == "Y":
        for node in listToParent:
            printBoard(node.getBoard())
            print("\n")


main()
#print(accManhattenDistance(getRandomBoard()))
