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


#Time complexity: O(b^m) where b is
#the branching factor and m the maximum depth
#of a node.
#Space complexity: O(bm)
def dfs(start, target):
    visited = []
    stack = [start]

    while stack:
    	vertex = stack.pop()

    	if vertex not in visited:
    		visited.append(vertex)
	    	if vertex == target:
	    		return visited

		for i in range(len(g[vertex])):
			if g[vertex][i][0] not in visited:
				stack.append(g[vertex][i][0])

    return None

#Tests
makeConnection('Miami', 'New York',250)
makeConnection('Miami', 'Hialeah', 5)
makeConnection('Hialeah', 'San Francisco', 200)
makeConnection('San Francisco','LA', 400)


bfsList = bfs('Miami', 'New York')
dfsList = dfs('Miami', 'New York')


print "======================================================="
print "======================================================="

print bfsList
print dfsList

print "======================================================="
print "======================================================="


# Print all nodes and edgess
for key, value in g.iteritems():
	print str(key) + ': ' + str(value)