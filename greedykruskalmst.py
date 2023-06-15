# Find set of vertex i
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i
 
# Does union of i and j. It returns false if i and j are already in same set.
def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b
 
# Finds MST using Kruskal's algorithm
def greedy_kruskal_mst(cost):
    mincost = 0 # Cost of min MST
 
    # Initialize sets of disjoint sets
    for i in range(V):
        parent[i] = i
 
    # Include minimum weight edges one by one
    edge_count = 0
    while edge_count < V - 1:
        min = INF
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if find(i) != find(j) and cost[i][j] < min:
                    min = cost[i][j]
                    a = i
                    b = j
        union(a, b)
        print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min))
        edge_count += 1
        mincost += min
 
    print("Minimum cost= {}".format(mincost))
 
V = 7
parent = [i for i in range(V)]
INF = float('inf')
cost = [[INF, 7, INF, 5, INF, INF, INF],
         [7, INF, 8, 9, 7, INF, INF],
         [INF, 8, INF, INF, 5, INF, INF],
         [5, 9, INF, INF, 15, 6, INF],
         [INF, 7, 5, 15, INF, 8, 9],
         [INF, INF, INF, 6, 8, INF, 11],
         [INF, INF, INF, INF, 9, 11, INF]]
 
# Print the solution
greedy_kruskal_mst(cost)