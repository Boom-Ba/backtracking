##build a BT with parent array
##index represents ith node, value represents its parent

def builtT():
  parent=[-1, 0, 0, 1, 2, 2, 4, 4]

  #{0:-1,1:0}
  d= {i: Node(i) for i in range(len(parent))}
  for node, parent in enumerate(parent):
    #node - index, its parent: parent[index]
    if parent==-1:
      root =d[node]
    else:
      par = d[parent]
      if par.right==None:
        par.right=d[node]
      else:
        par.left=d[node]
  return root

def printR(root):
  if root:
    print(root.val)
  
    printR(root.left)
    printR(root.right)

printR(root)
print(d)
#     0
#   1  2
#  3   4 5
#      6 7
