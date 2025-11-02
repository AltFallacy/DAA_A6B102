def NextValue(G, path, k, n):
    while True:
        path[k] = (path[k] + 1) % n
        if path[k] == 0:
            return
        if G[path[k - 1]][path[k]] != 0:
            for j in range(k):
                if path[j] == path[k]:
                    break
            else:
                if k < n - 1 or (k == n - 1 and G[path[k]][path[0]] != 0):
                    return
def hamiltonian(G, path, k, n):
    while True:
        NextValue(G, path, k, n)
        if path[k] == 0:
            return
        if k == n - 1:
            print(path)
        else:
            hamiltonian(G, path, k + 1, n)
adj=[
  [0,1,1,0,1],
  [1,0,1,1,0],
  [1,1,0,1,0],
  [0,1,1,0,1],
  [1,0,0,1,0]]
n=len(adj)
path=[0]*n
hamiltonian(adj,path,1,n)
