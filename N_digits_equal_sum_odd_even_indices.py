##find all digit number with equal sum of even and odd indices
##3-digit numbers ex: 110 121 
def find(n,res='',diff=0):
  if n>0:
    num= 0
    while num<=9:
      if n&1:
        diff+=num
      else:
        diff-=num
      find(n-1,str(num)+res,diff)
        # return True
      num+=1 
  elif n==0 and diff ==0:
    print(res)
    return True
n =3 
find(n)
"""
000,011,022,033,044,055,066,077,088,099,110,220,232,330,365,440,550,563,586,660,685,770,880,990
"""
