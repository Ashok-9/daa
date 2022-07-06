process=input("enter the id:").split()
pro=list(map(int,input("enter the profit:").split()))
deadline=list(map(int,input("enter the deadlines:").split()))
job=[]
for i in range(len(process)):
    job.append([process[i],pro[i],deadline[i]])
job.sort(key=lambda x:x[1],reverse=True)

m=max(deadline)
l=[0]*m
profit=0
for i in range(len(job)):
    k=job[i][2]
    while(k!=-1):
        if l[k-1]==0:
            l[k-1]=job[i][0]
            profit+=job[i][1]
            break
        else:
            k-=1
print(l)
print(profit)