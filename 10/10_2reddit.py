adapters = [int(v) for v in open("day10.txt")]
adapters.append(max(adapters) + 3)
adapters.append(0)
adapters.sort()

# part 1

differences = [v2 - v1 for v1, v2 in zip(adapters[:-1], adapters[1:])]
differences.count(1),  differences.count(3)
print(differences.count(1) * differences.count(3))

# part 2

class Graph:
    
    def __init__(self, values):
        self.values = values
        self.N = len(self.values)
        self.adjacencies = [list() for _ in range(self.N)]
        
        for i in range(self.N):
            for j in range(i + 1, self.N):
                u, v = self.values[i], self.values[j]
                if v - u <= 3:
                    self.adjacencies[i].append(j)
                else:
                    continue
    
    def get_removables(self):
        removables = set()
        for adj_list in self.adjacencies:
            if len(adj_list) > 1:
                removables = removables.union(adj_list[:-1])
        return list(removables)
    
    def check_solution(self, solution):
        new_values = [self.values[i] for i in range(self.N) if i not in solution]
        for v1, v2 in zip(new_values[:-1], new_values[1:]):
            if v2 - v1 > 3:
                return False
        return True
        
    def get_cuts(self):
        cuts = []
        l1_count = 0
        for i, adj_list in enumerate(self.adjacencies):
            if len(adj_list) == 1:
                l1_count += 1
            else:
                l1_count = 0
            if l1_count == 2:
                l1_count = 0
                cuts.append(i + 1)
        return cuts
    
    def find_solution(self):
        solution_count = 1 # zero-solution is always a solution
        removables = self.get_removables()
        stack = [[r] for r in removables]
        while stack:
            this_sol = stack.pop()
            if self.check_solution(this_sol):
                solution_count += 1
                k = this_sol[-1]
                for l in filter(lambda v: v > k, removables):
                    stack.append(this_sol + [l])
                    
        return solution_count
                
g = Graph(adapters)
g.get_cuts()

subgraphs = []
cuts = g.get_cuts()
subgraphs.append(Graph(adapters[:cuts[0]]))
for c1, c2 in zip(cuts[:-1], cuts[1:]):
    subgraphs.append(Graph(adapters[c1:c2]))
subgraphs.append(Graph(adapters[cuts[-1]:]))

solutions = 1
for sg in subgraphs:
    solutions *= sg.find_solution()
print(solutions)