def print_N_quene():
  N=8
  mat =[['-' for _ in range(N)] for _ in range(N)]
  
  col=set()
  dia =set()
  dia_2=set()
  #i-j i+j
  res=[]
  def dfs(i): 
    if i ==N:
      t=[''.join(i) for i in mat]
      res.append(t)
      return 
    
    for c in range(N):
      if c in col or (i+c) in dia or (i-c) in dia_2:
        continue
      mat[i][c]='Q'
      col.add(c)
      dia.add(i+c)
      dia_2.add(i-c)
      dfs(i+1)
      col.remove(c)
      dia.remove(i+c)
      dia_2.remove(i-c)
      mat[i][c]='-'
    
  dfs(0)
  return len(res)
print_N_quene()   
