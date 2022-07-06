
def merge(p_w):
    if len(p_w)>1:
        left=p_w[:len(p_w)//2]
        right=p_w[len(p_w)//2:]
        merge(left)
        merge(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i][3]>right[j][3]:
                p_w[k]=left[i]
                i=i+1
                k=k+1
            else:
                p_w[k]=right[j]
                j=j+1
                k=k+1
        while i<len(left):
            p_w[k]= left[i]
            i = i + 1
            k = k + 1
        while j<len(right):
            p_w[k] = right[j]
            j = j + 1
            k = k + 1

w=[eval(x) for x in input("Enter weights:").split()]
p=[eval(x) for x in input("Enter profits:").split()]
m=int(input("max capacity:"))
n=len(w)
p_w=[]
tw=0
tp=0
sol=[0]*n
for i in range(n):
    p_w.append([i,p[i],w[i],p[i]/w[i]])
merge(p_w)
print(p_w)


