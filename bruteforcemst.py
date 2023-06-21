import itertools
import time

def generate_edges(graph):
    edges = []
    num_vertices = len(graph)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    return edges

def calculate_cost(graph, edges):
    cost = 0
    for u, v, weight in edges:
        cost += weight
    return cost

def brute_force_mst(graph):
    num_vertices = len(graph)
    min_cost = float('inf')
    min_tree = []

    # Generate all possible combinations of edges
    edges = generate_edges(graph)

    # Generate all possible subsets of edges
    subsets = []
    for r in range(num_vertices - 1, len(edges) + 1):
        subsets.extend(itertools.combinations(edges, r))

    # Iterate through all possible subsets
    for subset in subsets:
        # Check if the current subset forms a valid tree
        vertices = set()
        for edge in subset:
            vertices.add(edge[0])
            vertices.add(edge[1])

        if len(vertices) == num_vertices:
            # Calculate the cost of the current tree
            cost = calculate_cost(graph, subset)

            # Update minimum cost and tree if necessary
            if cost < min_cost:
                min_cost = cost
                min_tree = subset

    return min_tree, min_cost


# Example usage
graph = [
    [0, 3, 6, 0, 0, 0, 0],
    [3, 0, 2, 4, 0, 0, 0],
    [6, 2, 0, 1, 4, 2, 0],
    [0, 4, 1, 0, 2, 0, 4],
    [0, 0, 4, 2, 0, 2, 1],
    [0, 0, 2, 0, 2, 0, 1],
    [0, 0, 0, 4, 1, 1, 0],
]

minimum_spanning_tree, minimum_cost = brute_force_mst(graph)

print("Minimum Spanning Tree:")
for u, v, weight in minimum_spanning_tree:
    print(f"{u} -- {v} (Weight: {weight})")
print("Minimum Cost:", minimum_cost)

end_time = time.time()
final_time = end_time - start_time
print("Processing Time:", final_time)
