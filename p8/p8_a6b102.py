def isSafe(node, graph, color, c):
    for i in range(len(graph)):
        if graph[node][i] == 1 and color[i] == c:
            return False
    return True

def graphColoringUtil(graph, m, color, node):
    if node == len(graph):
        return True
    for c in range(1, m + 1):
        if isSafe(node, graph, color, c):
            color[node] = c
            if graphColoringUtil(graph, m, color, node + 1):
                return True
            color[node] = 0
    return False

def solveGraphColoring(graph, m, labels):
    color = [0] * len(graph)
    if not graphColoringUtil(graph, m, color, 0):
        print("No valid color assignment")
        return
    for i in range(len(graph)):
        print(labels[i], ": Color", color[i])
graph1 = [
    [0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0]
]
labels1 = ['A', 'B', 'C', 'D', 'E', 'F']
print("Graph 1 Coloring:")
solveGraphColoring(graph1, 3, labels1)


graph2 = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]
]
labels2 = ['A', 'B', 'C', 'D', 'E']
print("\nGraph 2 Coloring:")
solveGraphColoring(graph2, 5, labels2)
