# Prim's Algorithm

INF = 9999999
Vertices = 4
Graph = [[0, 9, 75, 0],
         [9, 0, 95, 19],
         [75, 95, 0, 51],
         [0, 19, 51, 0]]

selected = [0, 0, 0, 0]
no_edge = 0
selected[0] = True
print("Edge : Weight")
while (no_edge < Vertices - 1):
    minimum = INF
    x = 0
    y = 0
    for i in range(Vertices):
        if selected[i]:
            for j in range(Vertices):
                if((not selected[j] and Graph[i][j])):
                    if minimum > Graph[i][j]:
                        minimum = Graph[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(Graph[x][y]))
    selected[y] = True
    no_edge += 1
