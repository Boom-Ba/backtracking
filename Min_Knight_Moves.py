from collections import deque
def shortest_distance(src,des,n,visited):
  q =deque()
  q.append([src,0])
  visited.add(src)
  while q:
    (x,y),steps=q.popleft()
    if (x,y) ==des:
      return steps
    for (nx,ny) in [(x+2,y-1),(x+2,y+1),(x-2,y+1),(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2)]:
      if 0<=nx<N and 0<=ny<N and (nx,ny) not in visited:
        q.append([(nx,ny),steps+1])

#minimum knight moves
if __name__ =='__main__':
  N = 8 #8by8 mat
  src=(0,7)
  des=(7,0)
  visited=set()
  res=shortest_distance(src,des,N,visited)
