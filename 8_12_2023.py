from collections import defaultdict

graph = defaultdict(list)

def addEdge(graph, u, v):
    graph[u].append(v)

def generateEdges(graph):
    edges = []

    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    
    return edges


input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".splitlines()



def part1(input):
    movement = input[0]
    values = input[2:]

    for val in values:
        nodeS, val = val.split(" = ")
        leftNode, rightNode = val.split(", ")
        leftNode = leftNode[1:]
        rightNode = rightNode[:2]

        addEdge(nodeS, leftNode)
        addEdge(nodeS, rightNode)

    

print(part1(input))