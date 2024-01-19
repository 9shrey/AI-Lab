Maze = [
['#', '#', '#', '_', '#', '#', '#', '#', '#', '%', '#'],
['#', '1', '.', '2', '.', '3', '#', '4', '.', '5', '#'],
['#', '.', '#', '#', '#', '.', '#', '#', '#', '.', '#'],
['#', '6', '#', '7', '.', '8', '#', '9', '.', '10', '#'],
['#', '.', '#', '#', '#', '#', '#', '.', '#', '.', '#'],
['#', '11', '.', '12', '#', '13', '.', '14', '#', '15', '#'],
['#', '#', '#', '.', '#', '#', '#', '.', '#', '.', '#'],
['#', '16', '.', '17', '.', '18', '.', '19', '#', '20', '#'],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

stack = []
#printing the maze
def printMaze(Maze):
	for i in range(9):
		for j in range(11):
			print(Maze[i][j], end="\t")
		print()

def stepDFS(Maze):
	for i in range(9):
		for j in range(11):
			if(Maze[i][j]=='_'):
				DFS(i,j)
		print()

def DFS(i,j):
	if(Maze[i-1][j]=='%'):
		exit(0)
	if((Maze[i][j+1]==';' or Maze[i][j+1]=='#') and (Maze[i][j-1]==';' or Maze[i][j-1]=='#') and (Maze[i+1][j]==';' or Maze[i+1][j]=='#') and (Maze[i-1][j]==';' or Maze[i-1][j]=='#')):
		stack.pop()
		stack.pop()
		print(stack.pop(), end =" ")
	if(Maze[i][j-1] == '.' or Maze[i][j-1].isnumeric()):
		print(Maze[i][j-1], end=" ")
		stack.append(Maze[i][j-1])
		Maze[i][j-1] = ';'
		DFS(i,j-1)

	if(Maze[i][j+1] == '.' or Maze[i][j+1].isnumeric()):
		print(Maze[i][j+1], end=" ")
		stack.append(Maze[i][j+1])
		Maze[i][j+1] = ';'
		DFS(i,j+1)

	if(Maze[i-1][j] == '.' or Maze[i-1][j].isnumeric()):
		print(Maze[i-1][j], end=" ")
		stack.append(Maze[i-1][j])
		Maze[i-1][j] = ';'
		DFS(i-1,j)

	if(Maze[i+1][j] == '.' or Maze[i+1][j].isnumeric()):
		print(Maze[i+1][j], end=" ")
		stack.append(Maze[i+1][j])
		Maze[i+1][j] = ';'
		DFS(i+1,j)



		

def main():
	printMaze(Maze)
	stepDFS(Maze)



if __name__=="__main__":
	main()
