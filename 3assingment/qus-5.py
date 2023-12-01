#  How will you compare two lists?

def Compare(l1,l2):
   l1.sort()
   l2.sort()
   if(l1==l2):
      return "Equal"
   else:
      return "Non equal"
l1=[1,2,3]
l2=[2,1,3]
print("First comparison",Compare(l1,l2))

l3=[1,2,3]
l4=[1,2,4]
print("Second comparison",Compare(l3,l4))
