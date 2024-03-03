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

def TSP(graph):
  start_node = list(graph.keys())[0]  
  current_node = start_node
  visited = set([start_node])
  distance = [start_node]
  total_distance = 0

  while len(visited) < len(graph):  
      nearest = None
      min_distance = float('inf')
      for neighbor, dist in graph[current_node].items():
          if neighbor not in visited:
            if dist < min_distance:
              min_distance = dist
              nearest = neighbor
      total_distance += min_distance
      visited.add(nearest)
      current_node = nearest
      distance.append(nearest)

  total_distance += graph[current_node][start_node]
  distance.append(start_node)

  return total_distance, distance

def solution(filename, total_distance, distance):
  with open(filename, 'w') as file:
      file.write(f"Total distance: {total_distance:.2f}")
      file.write("\n")
      file.write(" ".join(map(str, distance[:-1])))
      

graph = read_file("1000_euclidianDistance.txt")
total_distance, distance1 = TSP(graph)
solution("solution_922852718_A.txt", total_distance, distance1)

graph2 = read_file("1000_randomDistance.txt")
total_distance2, distance2 = TSP(graph2)
solution("solution_922852718_B.txt", total_distance2, distance2)
