import csv

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
						children.append(cities[j-1])
					j = j + 1
				node.append(children)
				graphList.append(node)
			i = i+1
		graph = dict(graphList)
		return graph




def main():
	graph = buildGraph('Assign2_MapMatrix.csv')
	print graph
	

if __name__ == "__main__":
	main()