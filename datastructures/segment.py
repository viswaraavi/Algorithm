import math

array = [2, 3, 4, 5, 6, 7]

no1 = 2 ** int(math.log(len(array), 2) + 1)

segment_tree = [-1] * (no1 * 2)




def construct_segmenttree(node, b, e, array, segment):
    if (b == e):
        segment[node] = b
    else:
        construct_segmenttree(2 * node, b, math.floor((b + e) / 2), array, segment)
        construct_segmenttree(2 * node + 1, math.ceil((b + e) / 2), e, array, segment)
        if (array[int(segment[2 * node])] <= array[int(segment[2 * node + 1])]):
            segment[node] = segment[2 * node]
        else:
            segment[node] = segment[2 * node + 1]


construct_segmenttree(1, 0, len(array) - 1, array, segment_tree)

def query(node,b,e,array,segment,i,j):

    if(i>e or j<b):
        return -1

    if(b>=i and  e<=j):

        return segment[node]

    p1=query(2 * node, b, math.floor((b + e) / 2), array, segment,i,j)
    p2=query(2 * node + 1, math.ceil((b + e) / 2), e, array, segment,i,j)

    if(p1==-1):
        segment[node]=p2
        return p2
    if(p2==-1):
        segment[node]=p1
        return p1 
    if(A[p1]<=A[p2]):
        segment[node]=p1
        return p1
    segment[node]=p2
    return p2

print query(1,0,len(array-1),array,segment_tree,1,4)
    
    
    








