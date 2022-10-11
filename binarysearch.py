def binarysearch(l,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return-1
l=[]
n=int(input("enter no.of elements"))
print("enter elements:")
for i in range(n):
    e=int(input())
    l.append(e)
    l.sort()
key=int(input("enter the element to be found :"))
low=0
result=binarysearch(l,low,n-1,key)
if result==-1:
    print("elements not found")
else:
    print("element found at :",result)