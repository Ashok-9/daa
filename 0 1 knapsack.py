p=[eval(x) for x in input('enter the profit:').split()]
wt=[eval(x) for x in input('weights:').split()]
m=int(input("Enter max capacity:"))
n=len(p)
k=[[0 for row in range(m+1)]for j in range(n+1)]
print(k)
sol=[0]*n
for row in range(n+1):
    for col in range(m+1):
        if(row==0 or col==0):
            k[row][col]=0
        elif(wt[row-1]<=col):
            k[row][col]=max(p[row-1]+k[row-1][col-wt[row-1]],k[row-1][col])
        else:
            k[row][col]=k[row-1][col]
    print(k)
print(k[n][col])
row,col=n,m
while(row>0 and col>0):
    if(k[row][col]!=k[row-1][col]):
        sol[row-1]=1
        col=col-wt[row-1]
        row=row-1
    else:
        row=row-1
print(sol)