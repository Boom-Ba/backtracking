'''

Given a set S, 
return all distinct subsets of it
Input : S[] = [1, 2, 1]
Output: [[1, 1, 2], [1, 2], [2], [1, 1], [1], []]

'''

class Solution:
	def findPowerSet(self, S: List[int]) -> List[List[int]]:
		powerset = []
    #purpose of sorting is pruing adjacent duplicates 
		S.sort()
  
		def solve(S,j,curr=[]):
			if j==len(S):
				t=curr.copy()
				powerset.append(t)
				return 

			#include element, no pruing 
			curr.append(S[j])
			solve(S, j+1, curr)
			curr.pop()
			
      #exclude an elemenet needs pruing because it gets same result for duplicates 
      ##pruing
			while j+1<len(S) and S[j]==S[j+1]:
				j+=1
      #after pruing, do exclude 
			solve(S,j+1,curr)
		solve(S,0)
		return powerset
