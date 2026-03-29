from collections import deque
import heapq

#BFS 
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
               queue.append(path + [neighbor])

# DFS
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(path + [neighbor])

# A*
def astar(graph, start, goal, heuristic):
    queue = [(heuristic[start], 0, [start])]  # (f, g, path)

    while queue:
        f, cost, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path

        for neighbor, weight in graph[node]:
            g = cost + weight
            h = heuristic.get(neighbor, 0)
            f_new = g + h
            heapq.heappush(queue, (f_new, g, path + [neighbor]))

    return []

# Hill Climbing
def hill_climbing(graph, start, goal, heuristic):
    current = start
    path = [current]
    while current != goal:
        neighbors = graph[current]
        next_node = min(neighbors, key=lambda x: heuristic.get(x, float('inf')))
        if heuristic[next_node] >= heuristic[current]:
            return path
        current = next_node
        path.append(current)
    return path

# Logic
def choose_algorithm(bfs_path, dfs_path, astar_path, hill_path):
    paths = {
        "BFS": bfs_path,
        "DFS": dfs_path,
        "A*": astar_path,
        "Hill": hill_path
    }
    return min(paths, key=lambda x: len(paths[x]))

# Bayes
def bayes(p, l, e):
    return (p * l) / e if e != 0 else 0

# Data
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}

weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('E', 1)],
    'D': [('E', 1)],
    'E': []
}

heuristic = {
    'A': 3, 'B': 2, 'C': 1, 'D': 1, 'E': 0
}

# Run
bfs_path = bfs(graph, 'A', 'E')
dfs_path = dfs(graph, 'A', 'E')
astar_path = astar(weighted_graph, 'A', 'E', heuristic)
hill_path = hill_climbing(graph, 'A', 'E', heuristic)

print("BFS:", bfs_path)
print("DFS:", dfs_path)
print("A*:", astar_path)
print("Hill:", hill_path)

best = choose_algorithm(bfs_path, dfs_path, astar_path, hill_path)
print("Chosen:", best)

print("Confidence:", round(bayes(0.6, 0.7, 0.5), 2))

print("\n--- Analysis ---")
print("BFS: shortest path in steps")
print("DFS: explores deeper paths")
print("A*: optimal using cost + heuristic")
print("Hill Climbing: greedy, may get stuck in local optimum")