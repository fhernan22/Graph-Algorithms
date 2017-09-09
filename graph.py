g = {}


# O(V + E) average
def makeConnection(node1, node2, w):
	if not g.has_key(node1):
		g[node1] = []

	

	if not g.has_key(node2):
		g[node2] = []

	updateNode(node1, node2, w)
	updateNode(node2, node1, w)


def updateNode(node1, node2,  w):
	for edge in range(len(g.get(node1))):
		if node2 == g.get(node1)[edge][0]:
			g.get(node1)[edge] = (node2, w)
			return

	g[node1].append((node2, w))


#Return a list containing all the nodes
#in the path from start to target if such
#path exists. None otherwise
#Generates b^d nodes in the worst case
#Optimal: yes, Complete: yes
def bfs(start, target):
    visited = [start]
    queue = [start]
    path = [start]

    while queue:
        vertex = queue[0]
        
        queue.remove(queue[0])

        for edge in range(len(g[vertex])):
            if g[vertex][edge][0] == target:
                path.append(g[vertex][edge][0])
                return path
            
            if not g[vertex][edge][0] in visited:
                visited.append(g[vertex][edge][0])
                queue.append(g[vertex][edge][0])
                path.append(g[vertex][edge][0])
                

    return None




makeConnection('Miami', 'New York',250)
makeConnection('Miami', 'New York', 20)
makeConnection('Miami', 'Hialeah', 5)
makeConnection('Hialeah', 'San Francisco', 200)
makeConnection('Miami','LA', 400)
makeConnection('Miami','LA', 42220)
makeConnection('Miami','LA', 3)




# Print all nodes and edgess
for key, value in g.iteritems():
	print key + ': ' + str(value)