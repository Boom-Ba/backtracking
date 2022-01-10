##print all possible knights tours on a chessboard
#start from (0,0) top-left corner 
def knight_tour(visited,x,y,pos,N):
  #mask as visited
  visited[x][y] =pos
  #print res
  if pos >= N*N:
    print(visited)
    # visited[x][y] =0
    # return 

  for (nx,ny) in [(x+2,y-1),(x+2,y+1),(x-2,y+1),(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2)]:
    if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
      knight_tour(visited,nx,ny,pos+1, N)
  visited[x][y]=0
if __name__ =='__main__':
  n=5
  (x,y) =(0,0)
  visited= [[0 for _ in range(n)] for _ in range(n)]
  knight_tour(visited,x,y,1,n)
