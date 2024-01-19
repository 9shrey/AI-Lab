Maze={
	1:[2,6],
	2:[0,1,3],
	3:[2,8],
	4:[5],
	5:[0,4,10],
	6:[1,11],
	7:[8],
	8:[3,7],
	9:[10,14],
	10:[5,9,15],
	11:[6,12],
	12:[11,17],
	13:[14],
	14:[9,13,19],
	15:[10,20],
	16:[17],
	17:[12,16,18],
	18:[17,19],
	19:[14,18],
	20:[15],
	0:[2,5]
}


stack = [-1,-1]
# #printing the maze
# def printMaze(Maze):
# 	for i in range(len(Maze)):
# 		for j in range(len(Maze[i])):
# 			print(Maze[i][j], end="\t")
# 		print()

def DFSFnc(vertex, visited):
		
		visited.add(vertex)
		print(vertex, end= ' ')
		for n in Maze[vertex]:
			if vertex == 5:
				exit(0)
			
			if n not in visited:
								# for i in range(len(Maze[vertex])):
				# 	if Maze[vertex][i] not in visited:
				# 		print(Maze[vertex][i], end="\t")
				DFSFnc(n, visited)
				stack.append(n)

			if n in visited:
				stack.append(n)
				if(stack.pop(0) in Maze[vertex]): 
					print(stack.pop(0), end="* ")
				
				
def DFS(v):
		visited = set()
		
		DFSFnc(v,visited)

def main():
	# printMaze(Maze)
	DFS(0)


if __name__=="__main__":
	main()
