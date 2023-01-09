
def aStarAlgo(start_node,end_node):
    open_set = set(start_node)
    close_set = set()
    parent = {}
    parent[start_node] = start_node
    dis = {}
    dis[start_node] = 0
    while len(open_set) > 0 :
        
        n = None
        
        for v in open_set:
            #print(v)
            if n == None or dis[v] + heuristic(v) < dis[n] + heuristic(n):
                n = v
            
        if n == end_node or Graph_nodes[n] == None:
            pass
        else:
            
            for (v, weights) in Graph_nodes[n]:
                
                if v not in open_set and v not in close_set:
                    dis[v] = dis[n] + weights
                    open_set.add(v)
                    parent[v] = n
                    #print(v)
                else:
                    
                    if(dis[v] > dis[n] + weights):
                        dis[v] = dis[n] + weights
                        parent[v] = n
                        
                        if v in close_set:
                            close_set.remove(v)
                            open_set.add(v)
            
                                
        if n == None:
                print('Path not found')
                return None
            
        if(n == end_node):
                
                path = []
                
                while parent[n] != n:
                    path.append(n)
                    n = parent[n]
                path.append(n)
                print(path)
                
                return
        
        
        open_set.remove(n)
        close_set.add(n)
        
    
    print('Path does not exist')
    return None
                
                
                

def heuristic(n):
 H_dist = {
 'A': 11,
 'B': 6,
 'C': 5,
 'D': 7,
 'E': 3,
 'F': 6,
 'G': 5,
 'H': 3,
 'I': 1,
 'J': 0 
 }
 return H_dist[n]
#Describe your graph here 
Graph_nodes = {
 'A': [('B', 6), ('F', 3)],
 'B': [('C', 3), ('D', 2)],
 'C': [('D', 1), ('E', 5)],
 'D': [('C', 1), ('E', 8)],
 'E': [('I', 5), ('J', 5)],
 'F': [('G', 1),('H', 7)] ,
 'G': [('I', 3)],
 'H': [('I', 2)],
 'I': [('E', 5), ('J', 3)], 
}
aStarAlgo('A', 'J')


