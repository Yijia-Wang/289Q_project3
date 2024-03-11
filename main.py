import time

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()[2:]  
        graph = {}
        for line in lines:
            split = line.split()  
            node1, node2, distance = int(split[0]), int(split[1]), float(split[2])  
            if node1 not in graph:
                graph[node1] = {}
            graph[node1][node2] = distance  
            if node2 not in graph:
                graph[node2] = {}
            graph[node2][node1] = distance 
    return graph

def TSP(graph, time_limit=900): # 15 min
    start_time = time.time()
    current_node = list(graph.keys())[0]  
    visited = set([current_node])
    path = [current_node]
    total_distance = 0
    cycle_count = 0

    while len(visited) < len(graph) and (time.time() - start_time) < time_limit:
        nearest = None
        min_distance = float('inf')
        for neighbor, dist in graph[current_node].items():
            if neighbor not in visited and dist < min_distance:
                min_distance = dist
                nearest = neighbor
        total_distance += min_distance
        visited.add(nearest)
        current_node = nearest
        path.append(nearest)
        cycle_count += 1  

    if len(visited) == len(graph):
        total_distance += graph[current_node][path[0]] 
        path.append(path[0])  

    return path, total_distance, cycle_count

def solution(filename, path, total_distance, cycle_count):
    with open(filename, 'w') as file:
        file.write(" ".join(map(str, path[:-1])))  
    print(f"Total distance: {total_distance:.2f}")
    print(f"Number of cycles evaluated: {cycle_count:e}")

graph = read_file("1000_euclidianDistance.txt")
path1, total_distance1, cycle_count1 = TSP(graph)
solution("solution_922852718_A.txt", path1, total_distance1, cycle_count1)

graph2 = read_file("1000_randomDistance.txt")
path2, total_distance2, cycle_count2 = TSP(graph2)
solution("solution_922852718_B.txt", path2, total_distance2, cycle_count2)
