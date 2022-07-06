def topsort(g, vtx):
    degree = [0] * vtx
    for node in g:
        for adjnode in g[node]:
            degree[adjnode] += 1

    bfs = [i for i in range(vtx) if degree[i] == 0]
    for node in bfs:
        if g.get(node)!=None:
            for adjnode in g[node]:
                degree[adjnode] -= 1
                if degree[adjnode] == 0:
                    bfs.append(adjnode)
    return bfs
g = {}

vtx, e = map(int, input('enter no of vertices and edges:').split())
for i in range(e):
    u, v = map(int, input().split())
    if u in g.keys():
        l = g[u]
        l.append(v)
        g[u]=l
    else:
        g[u] = [v]
print(g)
topSort = topsort(g, vtx)
print(topSort)



#test case

#5 7
# 0 2
# 0 3
# 1 0
# 1 3
# 2 4
# 3 2
# 3 4