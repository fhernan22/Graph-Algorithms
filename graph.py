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