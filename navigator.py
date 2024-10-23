from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def find_path(self, start, end):
        # IMPLEMENT FUNCTION HERE
        self.my_maze=[]
        for row in range(len(self.navigator_maze)):
            grid_row = []
            for column in range(len(self.navigator_maze[0])):
                grid_row.append(0)
            self.my_maze.append(grid_row)


        for row in range(len(self.navigator_maze)):
            for column in range(len(self.navigator_maze[0])):
                if self.navigator_maze[row][column] == 1:
                    self.my_maze[row][column] = 1
                    
        if(self.my_maze[start[0]][start[1]]==1):
            raise PathNotFoundException
        if(self.my_maze[end[0]][end[1]]==1):
            raise PathNotFoundException
            
            
        stack=Stack()
        stack.push(start)
        
        while(stack.peek()!=end):
            current=stack.peek()
            x=current[0]
            y=current[1]
            if x+1<len(self.my_maze) and self.my_maze[x+1][y]==0:
                stack.push((x+1,y))
                self.my_maze[x][y]=1
            elif y+1<len(self.my_maze[0]) and self.my_maze[x][y+1]==0:
                stack.push((x,y+1))
                self.my_maze[x][y]=1
            elif x-1>=0 and self.my_maze[x-1][y]==0:
                stack.push((x-1,y))
                self.my_maze[x][y]=1
            elif y-1>=0 and self.my_maze[x][y-1]==0:
                stack.push((x,y-1))
                self.my_maze[x][y]=1
            else:
                self.my_maze[x][y]=1
                stack.pop()
                if stack.is_empty():
                    break
        if(stack.peek()==end):
            ans=[0]*stack.size()
            i=stack.size()-1
            while(i>=0):
                ans[i]=stack.pop()
                i-=1
#Just return the path, don't print it
            return ans
        raise PathNotFoundException
