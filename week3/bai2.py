a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
dta=(a[2]-a[0])*(a[3]-a[1])
dtb=(b[2]-b[0])*(b[3]-b[1])
dtc=(min(a[2],b[2])-max(a[0],b[0]))*(min(a[3],b[3])-max(a[1],b[1]))
if a[2]<=b[0] or b[2]<=a[0] or a[3]<=b[1] or b[3]<=a[1]:
    print(dta+dtb)
else:
    print(dta+dtb-2*dtc)