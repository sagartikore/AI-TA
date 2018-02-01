import sys
import math
from random import shuffle
from draw import drawPath
import graph_plot
from collections import defaultdict
import argparse
import random
import itertools

#########################################################################################################
################# Provided code #########################################################################
#########################################################################################################
cities = 0
nodeDict = {}
numberOfRuns = 5

class Node():
    def __init__(self,index, xc, yc):
        self.i = index
        self.x = xc
        self.y = yc


def generateFile(cities, seed):
    MIN = 0
    MAX = 5000   
    random.seed(seed)
    i = 1
    filename = "tsp"+str(cities)
    with open(filename, "w") as f:
        for _ in itertools.repeat(None, cities):
            f.write("{p} {p0} {p1}\n".format(p=i, p0=random.randint(MIN, MAX), p1=random.randint(MIN, MAX)))
            i = i + 1
    return filename


def takeInput(file):
    global cities
    f = open(file,'r').read().splitlines()
    cities = len(f)
    for a in f:
        m = a.split()
        i = int(m[0])
        x = float(m[1])
        y = float(m[2])
        nodeDict[i] = Node(i, x, y)
    return


def save2optNeighbours(tour):
    """ You can print the list on stdout to check if your getting correct 2opt-neighbours
        or look into 2optNeighbours.txt file in your current directory"""
    tourList = generate2optNeighbours(tour)
    print(tourList)
    filename = "2optNeighbours.txt"
    file = open(filename, 'w')
    for i in tourList:
        file.write("%s\n" % i)



def generateRandomTour(r2seed):
    global cities
    print("number of cities are ",cities)
    random.seed(r2seed)
    tour = [x for x in range(1,cities+1)]
    #print(tour)
    shuffle(tour)
    #print(tour)
    return tour

def getTourLength(tour):
    global cities
    if len(tour) == 0:
        return 0

    length = 0
    if len(tour) == 2:
        return getDistance(nodeDict[tour[0]],nodeDict[tour[1]])

    for x in range(len(tour)-1):
        length += getDistance(nodeDict[tour[x]],nodeDict[tour[x+1]]) 
    
    length += getDistance(nodeDict[tour[0]],nodeDict[tour[-1]])

    return length

def getDistance(n1, n2):
    return math.sqrt((n1.x-n2.x)*(n1.x-n2.x) + (n1.y-n2.y)*(n1.y-n2.y))

unionFind= [] 

def union(x,y):
    k1 = unionFind[x]
    k2 = unionFind[y]
    for x in range(cities+1):
        if unionFind[x] == k1:
            unionFind[x] = k2


def find(x,y):
    return unionFind[x] == unionFind[y]


#############################################################################################

def generate2optNeighbours(tour):
    global cities
    all_possible_neighbours = []

    "*** YOUR CODE HERE ***"
    order = tour
    for x in range(len(order)):
        for y in range(len(order)):
            if x < y:
                new_order = order[:x] + order[x:y][::-1] + order[y:]
                all_possible_neighbours.append(new_order)
    "*** --------------  ***"
    return all_possible_neighbours



def hillClimbFull(initial_tour):
    """ Use the given tour as initial tour, Use your generate2optNeighbours() to generate
        all possible 2opt neighbours and apply hill climbing algorithm. Store the tour lengths
        that you are getting after every hill climb step in the list tourLengthList.
        Store the minimum tour found after the hill climbing algorithms in minTour.
        Your code will return the tourLengthList and minTour.     
        You will find 'task2.png' in current directory which shows hill climb algorithm performace
        The tourLengthList will be used to generate a graph which plots tour lengths with each step.
        that is hill climb iterations against tour length"""

    global cities
    tourLengthList = []
    minTour = 0

    "*** YOUR CODE HERE ***"

    "*** --------------  ***"

    return tourLengthList, minTour


def nearestNeighbourTour(initial_city):
    tour = []

    "*** YOUR CODE HERE ***"
   


    "*** --------------  ***"

    return tour



def eucledianTour(initial_city):
    global unionFind, cities, nodeDict
    edgeList = []

    "*** YOUR CODE HERE ***"
   



    "*** --------------  ***"

    '''KRUSKAL's algorithm'''

    mst = []
    for x in range(cities+1):
        unionFind.append(x)
    
    edgeList.sort(key=lambda x:int(x[2]))
    for x in edgeList:
        if(find(x[0],x[1]) == False):
            mst.append((x[0],x[1]))
            union(x[0],x[1])

    '''FINISHES HERE'''



    fin_ord = finalOrder(mst, initial_city)
    return fin_ord

def finalOrder(mst, initial_city):
    "*** YOUR CODE HERE ***"
   



    "*** --------------  ***"



 
##################################################################################################
####### DO NOT CHANGE THIS CODE ###########################################################################
###########################################################################################################
def hillClimbWithNearestNeighbour(starting_city):
    tour = nearestNeighbourTour(starting_city)
    tourLengthList, min_tour = hillClimbFull(tour)
    return tourLengthList
    

def hillClimbWithEucledianMST(initial_city):
    tour = eucledianTour(initial_city)
    tourLengthList, minTour = hillClimbFull(tour)
    return tourLengthList



def hillClimbWithRandomTour(tour):
    tourLengthList = []
    tourLengthList, minTour = hillClimbFull(tour)
    return tourLengthList

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', action='store', dest='file', help="Provide a file name (if file given then no need to provide city and random seed option that is -n and -r)")
    parser.add_argument('--cities', '-n', action='store', type=int, dest='cities', help="Provide number of cities in a tour")
    parser.add_argument('-r1', action='store', type=int, dest='r1seed', default=1, help="random seed")
    parser.add_argument('-r2', action='store', type=int, dest='r2seed', default=1, help="random seed")
    parser.add_argument('--task', '-t', action='store', type=int, dest="task", help="task to execute")
    parser.add_argument('--starting_city', '-i', action='store', type=int, default=1, dest='starting_city', help="Initial city")
    parser.add_argument('--submit', action='store_true', help="final submission")

    args = parser.parse_args()

    if args.submit:
        takeInput("data/st70.tsp");
    elif args.file:
        takeInput(args.file)
    elif args.cities:
        file = generateFile(args.cities, args.r1seed)
        takeInput(file)
    else:
        print("Please provide either a file or combination of number of cities and random seed")
        sys.exit()

    if not args.task:
        print("Please provide task number to execute")
        sys.exit()


    if args.task == 1:
        tour = generateRandomTour(args.r2seed)
        save2optNeighbours(tour)

    if not args.submit:
        if args.task == 2:
            tour = generateRandomTour(args.r2seed)
            tourLengthList = hillClimbWithRandomTour(tour)
            graph_plot.generateGraph(tourLengthList, "task2.png")
        

        if args.task == 3:
            tourLengthList = hillClimbWithNearestNeighbour(args.starting_city)
            graph_plot.generateGraph(tourLengthList, "task3.png")


        if args.task == 4:
            tourLengthList = hillClimbWithEucledianMST(args.starting_city)
            graph_plot.generateGraph(tourLengthList, "task4.png")

    else:
        if args.task == 2:
            data = []
            for i in range(1, numberOfRuns+1):
                random_seed = i
                tour = generateRandomTour(random_seed)
                tourLengthList = hillClimbWithRandomTour(tour)
                data.append(tourLengthList)

            graph_plot.generateFinalGraph(data, "task2_submit.png", 2)

        if args.task == 3:
            data = []
            for i in range(1, numberOfRuns+1):
                starting_city = i
                tourLengthList = hillClimbWithNearestNeighbour(starting_city)
                data.append(tourLengthList)

            graph_plot.generateFinalGraph(data, "task3_submit.png", 3)

        if args.task == 4:
            tourLengthList = hillClimbWithEucledianMST(args.starting_city)
            graph_plot.generateGraph(tourLengthList, "task4_submit.png")
###################################################################################

