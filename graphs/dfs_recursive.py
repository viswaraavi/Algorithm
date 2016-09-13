graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(solution,start,graph):
    for i in graph[start]-solution:
        solution.add(i)
        print i
        dfs(solution,i,graph)


solution={'A'}
dfs(solution,'A',graph)

print "Iterative"

def dfs_iterative(start,graph):
    visited,stack=set(),[start]
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            print vertex
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)

dfs_iterative("A",graph)



def generate_adjacent(index1,index2,M):
    rows = len(M)
    cols = len(M[0])
    list1=[]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if(index1-i>=0 and index1-i<rows and index2-j>=0 and index2-j<cols and (i*j!=1) and (i*j!=-1) ):
                list1.append((index1-i,index2-j))
    candidates=[]
    for element in list1:
        if(M[element[0]][element[1]]==1):
            candidates.append(element)
    return candidates





M=[[1, 1, 0, 0, 0],[0, 1, 0, 0, 1],[1, 0, 0, 1, 1],[0, 0, 0, 0, 0], [1, 0, 1, 0, 1]]

def dfs_matrix(start,M):
    stack=[start]
    while (stack):
        element=stack.pop()
        if (M[element[0]][element[1]] != -1):
            adjacent = generate_adjacent(element[0],element[1],M)
            M[element[0]][element[1]] = -1
            stack.extend(adjacent)

count=0
for index1,row in enumerate(M):
    for index2,element in enumerate(row):
        if(M[index1][index2]==1):
            dfs_matrix([index1,index2],M)
            count=count+1

print count







