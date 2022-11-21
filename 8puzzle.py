import math
import sys
from queue import PriorityQueue
import time
from random import randrange 
from utilities import PrioQueue, ClosedQueue, SearchTree, getRandomBoard, printBoard, getLegalMoves, getCopy, doXRandomMoves, doMove, stringToBoard

#board = [[], [], []]

class Config:
    def __init__(self, config):
        if config == 1 or config == 2:
            self.config = config
        else:
            raise ValueError
    
    def getGoalConfig(self):
        if self.config == 1:
            return [[0,1,2], [3,4,5], [6,7,8]]
        if self.config == 2:
            return [[1,2,3], [4,5,6], [7,8,0]]
    
    def getFinalPositions(self):
        if self.config == 1:
            return [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        if self.config == 2:
            return [(2, 2), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]


try:
    GOAL_BOARD_CONFIGURATION = int(sys.argv[1])
except:
    print("Please enter a desired goal-configuration [1,2]; for example : python3 8puzzle.py 1")
    exit()

CONFIG = Config(GOAL_BOARD_CONFIGURATION)
FINAL_POSITIONS = CONFIG.getFinalPositions()
GOAL_CONFIG = CONFIG.getGoalConfig()

def accManhattenDistance(board):
    amd = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                continue
            amd += manhattenDistance(board[i][j], i, j)
    return amd

def manhattenDistance(n, currentI, currentJ):
    return int(math.ceil(
        math.sqrt(
            math.pow(currentI - FINAL_POSITIONS[n][0], 2) + 
            math.pow(currentJ - FINAL_POSITIONS[n][1], 2)
        )
    ))



#-----------------------------------------------------------Implementing the algorithm---------------------------

def isSolved(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != GOAL_CONFIG[i][j]:
                return False 
    return True

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
            doMove(bn, move)
            if not closedQueue.contains(bn):

                node = searchTree.insert(bn)
                node.setParent(current_tree_node)

                openQueue.insert(node.getDepth() + accManhattenDistance(bn), bn)
        closedQueue.insert(current_board)




def main():
    start_time = time.time()
    
    beginBoard = getRandomBoard()
    if len(sys.argv) > 2:
        beginBoard = stringToBoard(sys.argv[2])
    
    
    print("Starting-configuration : ")
    printBoard(beginBoard)
    print("\n------------------------------------\n")
    
    solutionNode = findSolution(beginBoard)
    listToParent = solutionNode.getListToParent()

    print("                  Amout moves to solve : {}".format(len(listToParent) - 1))
    print("                  Total Explored Nodes : {}".format(searchTree.getAmountNodes()))
    print("                  Time : %s seconds" % (time.time() - start_time))
    print("\n------------------------------------\n")

    answer = input("Print moves to solution? [Y/N]")
    if answer == "y" or answer == "Y":
        for node in listToParent:
            printBoard(node.getBoard())
            print("\n")


main()
