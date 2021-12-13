from os import sep


graph = {}

def traverse(root,double,visited=[],memo=[]):
    ways = 0
    if root == 'end':
        return 1

    for node in graph[root]:
        next_node = []
        if node in visited and not double:
            ways += traverse(node,True,visited,memo+[root])
        elif node not in visited:
            if node.lower() == node:
                next_node.append(node)
            ways += traverse(node,double,visited+next_node,memo+[root])
    return ways
    
    

with open('input.txt') as f:
    for line in f.readlines():
        left,right = line.strip().split('-',1)
        if right != 'start':
            if left not in graph.keys():
                graph[left] = [right]
            else:
                graph[left] = graph[left] + [right]
        if left != 'start':
            if right not in graph.keys():
                graph[right] = [left]
            elif left != 'start':
                graph[right] = graph[right] + [left]

n = traverse('start',False)
print(n)
