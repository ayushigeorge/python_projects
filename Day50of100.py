#DAY 50 OF 100 DAYS OF CODE
#IMPLEMENTING BINARY SEARCH ALGORITHM IN PYTHON PORGRAM

def binarysearch(a,x):
  low = 0
  high= len(a)-1
  mid =0
  while low<=high:
    if a[mid]<x:
      low= mid+1
      elif a>x:
        high= mid-1
       else:
        return mid
    return -1
  a= [90,78,93,86,45,4,10,40]
  x=10
  
  r= binarysearch(a,x)
  if result != -1:
    print("Element is present at: ",str (r))
  else:
    print("Element is not present in array!")
