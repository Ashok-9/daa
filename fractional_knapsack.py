
def merge(p):
    if len(p)>1:
        left=p[:len(p)//2]
        right=p[len(p)//2:]
        merge(left)
        merge(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i][3]>right[j][3]:
                p[k]=left[i]
                i=i+1
                k=k+1
            else:
                p[k]=right[j]
                j=j+1
                k=k+1
        while i<len(left):
            p[k] = left[i]
            i = i + 1
            k = k + 1
        while j<len(right):
            p[k] = right[j]
            j = j + 1
            k = k + 1
def knapsack(pw,max,n):
    res=[0]*n
    profit=0
    for i in range(n):
        if(pw[i][2]<=max):
            max=max-pw[i][2]
            profit=profit+pw[i][1]
            res[pw[i][0]]=1
        else:
            r=max/pw[i][3]
            profit=profit+pw[i][3]*r
            res[pw[i][0]]=r
            break
    print(profit)
    print(res)
w=[eval(x) for x in input("Enter weights:").split()]
p=[eval(x) for x in input("Enter profits:").split()]
max=int(input("enter the max capacity"))
n=len(w)
pw=[]
for i in range(len(p)):
    pw.append([i,p[i],w[i],p[i]/w[i]])
merge(pw)
knapsack(pw,max,n)