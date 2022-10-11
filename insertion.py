n=int(input("enter the number of elements in list:"))
l=[]
j=0
for i in range(0,n):
    ele=int(input("enter the element:"))
    l.append(ele)
print("list before sort:",l)
for i in range(1,len(l)):
     j=j-1
next_element=l[i]
while(l[i]>next_element)and j>=0:
    l[j+1]=l[j]
    j=j+1
    l[j+1]=next_element
print("list after sorting:",l)