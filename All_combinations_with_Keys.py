# ##find all combinations with the requirements
# list[1] —> { 'A', 'B', 'C', 'D' }
# list[2] —> { 'E', 'F', 'G', 'H', 'I', 'J', 'K' }
# list[3] —> { 'L', 'M', 'N', 'O', 'P', 'Q' }
# list[4] —> { 'R', 'S', 'T' }
# list[5] —> { 'U', 'V', 'W', 'X', 'Y', 'Z' }

# key =131
# Output:
 
# ALA AMA ANA AOA APA AQA BLB BMB BNB BOB BPB BQB CLC CMC CNC COC CPC CQC DLD DMD 
# DND DOD DPD DQD
def bt(res, lists, visited, keys,index,combs):
  if index==len (keys):
    combs.add(res)
    return 
  #which row we are at 
  num =keys[index]

  curr_list =lists[num]
  #PICK ONE ITEM IN LISTS[NUM]
  for j in range(len(curr_list)): 
    if curr_list[j] not in visited[num]:
      visited[num].append(curr_list[j])
      ##add to res 
      bt(str(lists[num][j])+res, lists, visited, keys,index+1,combs)
      visited[num].pop()

  return 
if __name__ =='__main__':
  lists = [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H', 'I', 'J', 'K'],
        ['L', 'M', 'N', 'O', 'P', 'Q'],
        ['R', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Y', 'Z']
    ]
 
    # input number in the form of a list
  keys = [0, 2, 0]

  visited={i:[] for i in range(len(lists))}
  # find and print all combinations
  combs=set()
  bt('', lists, visited, keys, 0, combs)
  print(combs)
