n=int(input())
d=dict()
ans=0
for i in range(0,n):
    x=input()
    d[x]=(d[x]+1 if x in d else 1)
print(max(d.keys(),key=lambda a: d[a]))