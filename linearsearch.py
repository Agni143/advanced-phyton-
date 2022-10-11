l=[]
n=int(input("enter no.of elements:"))
for i in range(n):
    e=int(input())
    l.append(e)
flag=0
x=int(input("enter the element to be found"))
for i in range(n):
    if l[i]==x:
        flag=1
        if flag==1:
            print("elements found at",i)
        else:
            print("element is not found")