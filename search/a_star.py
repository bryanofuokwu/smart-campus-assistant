import heapq

class Node:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors  # dict: neighbor -> cost

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, neighbors):
        self.nodes[name] = Node(name, neighbors)

    def heuristic(self, current, goal):
        # For demo purposes, return 0 to act like UCS. You can customize this.
        return 0

    def a_star(self, start, goal):
        open_set = [(0, start)]
        came_from = {}
        g_score = {node: float('inf') for node in self.nodes}
        g_score[start] = 0

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor, cost in self.nodes[current].neighbors.items():
                tentative_g = g_score[current] + cost
                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return None

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

if __name__ == "__main__":
    g = Graph()
    g.add_node("Library", {"Cafeteria": 1, "Lab": 4})
    g.add_node("Cafeteria", {"Library": 1, "Gym": 2})
    g.add_node("Lab", {"Library": 4, "Gym": 3})
    g.add_node("Gym", {"Cafeteria": 2, "Lab": 3, "LectureHall": 5})
    g.add_node("LectureHall", {"Gym": 5})

    path = g.a_star("Library", "LectureHall")
    print("Shortest path:", path)
