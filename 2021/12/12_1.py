graph = {}

def traverse(root,visited=[]):
    ways = 0
    if root == 'end':
        return 1
    
    for node in graph[root]:
        # if root == 'start':
        #     print("N: ", node)
        if node not in visited:
            # print(f"{root} -> {node} ({visited})")
            if ord(root[0]) in range(97,123):
                # visited.append(root)
                ways += traverse(node,visited+[root])
            else:
                ways += traverse(node,visited)
    return ways
    
    

with open('input.txt') as f:
    for line in f.readlines():
        # print(line.strip().split('-',1))
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

n = traverse('start')
print(n)
