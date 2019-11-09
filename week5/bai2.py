a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
aset=set(a)
bset=set(b)
for i in aset:
    if(i in bset): print(i,end=" ")