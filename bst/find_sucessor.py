import simple_binary_tree as bt
import math

"""
@find sucessor
"""
def find_min(node):
    while(node.left):
        node=node.left
    return node



def find_sucessor(node):

    if(node.right):
        return find_min(node.right)
    else:
        while(node.parent):
            temp=node
            node=node.parent
            if(node.left==temp):
                return node
        return None

"""
@search in bst
"""

def _search(node,k):
    if(node):
        return search_iterative(node,k)
    else:
        return None


def search(node,k):

    bool1=None
    bool2=None
    if(node.l_child and node.data>=k):
       bool1=search(node.l_child,k)
    if (node.data == k and not bool1):
        return node
    elif(node.r_child and node.data<k):
        bool2=search(node.r_child,k)

    return bool1 or bool2


def search_iterative(node,k):

    first=None

    while(node):
        if(node.data>k):
            node=node.l_child

        elif(node.data<k):
            node=node.r_child
        else:
            first=node
            node=node.l_child
    return first

def search_k(node,k):
    bool1=None
    bool2=None
    if(node.data>k):
        if(node.l_child):
            bool1=search_k(node.l_child,k)
        else:
            return None
    elif(node.data<=k):
        if(node.r_child):
            bool2=search_k(node.r_child,k)
        elif(node.data==k):
            return node
        else:
            return None
    if (node.data == k and not bool2):
        return node
    else:
        return bool2 or bool1

    return None



"""
Building a binary search tree from sorted array

"""

def build_tree(array):
    mid = int(len(array) / 2)
    node=bt.Node(array[mid])
    build_binary_search(array[:mid],node)
    build_binary_search(array[mid+1:],node)

    return node


def build_binary_search(array,node):

    if(array):
        mid=int(len(array)/2)
        bt.binary_insert(node,bt.Node(array[mid]))
        build_binary_search(array[:mid],node)
        build_binary_search(array[mid+1:],node)

"""
Constructing binary search tree from linked list

"""
def construct_binary(m,n):

    mid=int(n/2)
    node=bt.Node(mid)
    construct_binary_search(0,mid,node)
    construct_binary_search(mid,n,node)
    return node




def construct_binary_search(m,n,node):
    if (n-m >1):
        mid=m+int(math.ceil((n-m)/2))
        bt.binary_insert(node,bt.Node(mid))
        construct_binary_search(m,mid,node)
        construct_binary_search(mid,n,node)





"""

constructing double linked list from binary tree

"""

def double_linked_list(root):


    node_l=None
    node_r=None

    if(root.l_child):
        node_l=double_linked_list(root.l_child)


    if(root.r_child):
        node_r=double_linked_list(root.r_child)

    if(node_l):
        temp=root.l_child.r_child
        node_x=node_l
        while (temp):
            node_x=temp
            temp = temp.r_child

        root.l_child=node_x

        node_x.r_child=root

    if(node_r):
        temp1=root.r_child.l_child
        node_y=node_r
        while(temp1):
            node_y=temp1
            temp1=temp1.l_child

        root.r_child=node_y
        node_y.l_child=root

    return root



"""
merge two bsts
"""
def merge_bsts(root1,root2):
    pass

"""
First k largest elements in BST
"""

list1=[]
def k_largest(root,k=0):
    if(k<3):
        if(root.r_child):
            k_largest(root.r_child,len(list1))

        list1.append(root.data)

        if(root.l_child):
            k_largest(root.l_child,len(list1))




"""
Traversal orders in tree
Preorder traversal generates unique tree
The complexity of the first solution is o(n^2)
"""
class Node:

    def __init__(self,data,l_child=None,r_child=None):
        self.data=data

        self.l_child=l_child
        self.r_child=r_child


def traversal_orders(list1):
    if(list1):
        x=list1[0]
        list1.pop(0)
        root=Node(data=x)
        index1=0
        for index,i in enumerate(list1):
            if(i>x):
                index1=index
                break

        root.l_child=traversal_orders(list1[:index1])
        root.r_child=traversal_orders(list1[index1:])
        return root

"""
Trying to build with complexty O(n)
"""

def traversal_orders_n(list1):
    pass


"""
Nearest restaurent application of binary search tree
"""
list2=[]
def nearest_restaurent(root,l,u):

    if(root.data<l):
        nearest_restaurent(root.r_child,l,u)
    elif(root.data>u):
        nearest_restaurent(root.l_child,l,u)
    else:
        if(root.l_child and root.l_child.data>=l):
            nearest_restaurent(root.l_child,l,u)

        if(root.data>l and root.data<u):
            list2.append(root.data)

        if(root.r_child and root.r_child.data<=u):
            nearest_restaurent(root.r_child,l,u)

"""
Another application of bst


"""

def another_application(a=[],b=[],c=[]):
    pass




node=bt.Node(100)
bt.binary_insert(node,bt.Node(8))
bt.binary_insert(node,bt.Node(10))
bt.binary_insert(node,bt.Node(6))
bt.binary_insert(node,bt.Node(5))
bt.binary_insert(node,bt.Node(8))
bt.binary_insert(node,bt.Node(200))
bt.binary_insert(node,bt.Node(150))
bt.binary_insert(node,bt.Node(250))

nearest_restaurent(node,125,225)
print list2

#root=build_tree([1,2,3,4,5,6])

#k_largest(node)

#root=construct_binary(1,8)

#bt.in_order_print(root)

#x=double_linked_list(node)

#print list1

#x=traversal_orders([100,8,6,5,10,200,150,250])
#print x























