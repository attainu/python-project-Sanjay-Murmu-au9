import collections
import argparse # used for creating command-line
import copy # To copy visited arr

class Solution:
    def __init__(self,maze,start,destination):
        self.maze = maze
        self.start = start
        self.destination = destination

    def shortestDistanceBfs(self):
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        queue=collections.deque ([(self.start[0],self.start[1])])

        distances=[[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        distances[self.start[0]][self.start[1]]=1

        while queue:
            (x,y)=queue.popleft()

            for (dx,dy) in dirs:
                count=distances[x][y]
                nx = x
                ny = y
    
                while 0<=nx+dx<len(maze) and 0 <= ny + dy < len(maze[0]) and maze[nx+dx][ny+dy]==1:
                    nx += dx
                    ny += dy
                    count += 1
                    if distances[nx][ny]==0 or distances[nx][ny]> count:
                        distances[nx][ny]=count
                        queue.append((nx,ny)) 

        return distances[self.destination[0]][self.destination[1]]

    def SourceToDestination_Path(self, shortest_dis):
        global ans
        ans=-1
        n = len(self.maze)
        m = len(self.maze[0])
        visited = [[0 for i in range(m)] for j in range(n)]
        c = 1
        dfs(self.maze,self.start[0],self.start[1],n,m,self.destination[0],self.destination[1],visited,c,shortest_dis)
        return ans

def dfs(maze,x,y,n,m,dx,dy,visited,count,shortest_dis):
    global ans
    if x<0 or y<0 or x>=n or y>=m:
        return                              # base condition

    if visited[x][y]==1 or maze[x][y]==0:
        return 

    if x==dx and y==dy and count==shortest_dis:
        visited[x][y] = 1
        ans = copy.deepcopy(visited)
        return 

    visited[x][y] = 1 
    count += 1

    dfs(maze,x+1,y,n,m,dx,dy,visited,count,shortest_dis) # moving down
    dfs(maze,x,y+1,n,m,dx,dy,visited,count,shortest_dis) # Moving right
    dfs(maze,x-1,y,n,m,dx,dy,visited,count,shortest_dis) # moving up
    dfs(maze,x,y-1,n,m,dx,dy,visited,count,shortest_dis) # moving left

    visited[x][y] = 0 # if move wrong path then we will go back
    count -= 1

if __name__ == '__main__':   

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, default="input.txt", help='What is your input file name?')
    parser.add_argument('--output_file', type=str, default='output.txt', help='What is your output file name?')
    args = parser.parse_args()


    s=open(args.input_file,"r") # open methond to read a file
    maze=list()
    for data in s:
        maze.append(list(map(int, data.split())))
    s.close() # close file
    # print(maze)
    sol=Solution(maze,[0,0],[len(maze)-1,len(maze[0])-1])
    # sol = Solution(maze,[0,0],[3,3])
    shortest_dis = sol.shortestDistanceBfs()
    print("Shortest distance from source to",shortest_dis)
    print()
    path_followed = sol.SourceToDestination_Path(shortest_dis)
    # print(path_followed)
    # for i in path_followed:
    #     print(*i)
    w=open(args.output_file,"w") # open methond to read a file
    if path_followed==-1:
        w.write("-1")
        
    else:

        for data in path_followed:
            w.write(" ".join(map(str,data)))
            w.write("\n")

    w.close()