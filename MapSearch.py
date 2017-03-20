import csv

found = False
init = False

def buildGraph(csvpath):
	with open(csvpath, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		cities = []
		graphList = []
		i=0
		for row in reader:
			if i == 0 :
				cities = row[1:len(row)]
			else :
				node = []
				children = []
				j=0
				for item in row :
					if j == 0 :
						node.append(item)
					elif item == '1':
						if cities[j-1] != node[0] :
							children.append(cities[j-1])
					j = j + 1
				node.append(children)
				graphList.append(node)
			i = i+1
		graph = dict(graphList)
		return graph


def breadthFirstSearch(graph, start, end):
	path = []
	queue = [start]
	while queue:
		path = queue.pop(0)
		node = path[-1]
		if node == end:
			break
		for next in graph.get(node, []):
			new_path = list(path)
			new_path.append(next)
			queue.append(new_path)
	return path

def depthFirstSearch(graph, start, end, path=[]):
	path.append(start)
	print 'Visiting node ', start
	if start == end:
		global found
		found = True
		return path
	else:
		print 'Expanding ', start, ' to ', graph[start]
	for next in sorted(set(graph[start]) - set(path)):
		if found == True:
			break
		depthFirstSearch(graph, next, end, path)
	if found != True:
		path.pop()
	return path

def main():
	path = 'Assign2_MapMatrix.csv'

	while(1):
		print 'Loading %s would you like to use a different adjacency matrix .csv file path?' % (path)
		isNewPath = raw_input("[y/n]: ")
		if (isNewPath == 'y' or isNewPath == 'Y') :
			path = raw_input("Please enter file path to valid .csv file: ")
			break
		elif (isNewPath == 'n' or isNewPath == 'N') :
			break
		else:
			print 'Error: invalid selection\n'
		
	graph = buildGraph(path)


	while(1):
		start = raw_input('Enter the starting location: ')
		if start in graph:
			break
		print 'Error: desired starting location not in provided graph. Please try again.'
	
	while(1):
		end = raw_input('Enter the destination: ')
		if end in graph:
			break
		print 'Error: desired destination not a location in the provided graph. Please try again.'
	
	while(1):
		searchType = raw_input('Enter the desired search algorithm (BFS or DFS): ')
		if searchType == 'DFS' or searchType == 'dfs':
			path = depthFirstSearch(graph, start, end, [])
			print 'Found destination ', end, '!'
			print 'Path: ', path
			global found
			found = False
			break
		elif searchType == 'BFS' or searchType == 'bfs':
			path = breadthFirstSearch(graph, start, end)
			print 'Found destination ', end, '!'
			print 'Path: ', path
			break
		print 'Error: invalid selection, please try again.'

	print '--------------------'
	main()

if __name__ == "__main__":
	main()