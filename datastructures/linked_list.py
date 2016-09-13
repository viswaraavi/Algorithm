class node:
    def __init__(self,data,nextnode):
        self.data=data
        self.nextnode=nextnode

    def __str__(self):
        return str(self.data)

class doublenode:
    def __init__(self,data,nextnode,prevnode):
        self.data=data
        self.nextnode=nextnode
        self.prevnode=prevnode

    def __str__(self):
        return str(self.data)

class LinkedList:

    def __init__(self,data):
        self.head=node(data,None)

    def __str__(self):
        x=""
        next_node=self.head
        while(next_node):
            x=x+str(next_node.data)
            next_node=next_node.nextnode
        return x

    def insert(self,data):
        newnode=node(data,None)
        newnode.nextnode=self.head
        self.head=newnode

    def reverse(self):
        currentnode=self.head
        tmp=self.head.nextnode
        self.head.nextnode=None
        while(tmp):
            nextnode=tmp
            tmp2=tmp.nextnode
            tmp.nextnode=currentnode
            tmp=tmp2
            currentnode=nextnode
        self.head=currentnode

    def search(self,data):
        next_node=self.head
        while(next_node):
            if(next_node.data==data):
                return next_node
            next_node=next_node.nextnode
        return None

    def delete(self,data):
        next_node = self.head
        prevnode=self.head
        while (next_node):
            if (next_node.data == data):
                prevnode.nextnode=next_node.nextnode
            prevnode=next_node
            next_node = next_node.nextnode

    def randomacess(self,index):
        next_node=self.head
        while(index):
            next_node=next_node.nextnode
            index=index-1
        return next_node

    def append(self,data):
        next_node=self.head
        prev_node=self.head
        while(next_node):
            prev_node=next_node
            next_node=next_node.nextnode
        newnode=node(data,None)
        prev_node.nextnode=newnode
        newnode.nextnode=None

    def convert_to_double(self):
        newnode=doublenode(self.head.data,)
        next_node=self.head
        while(next_node):
            pass

    def merge_two_lists(self,another_list):
        next_node = self.head
        prev_node = self.head
        while (next_node):
            prev_node = next_node
            next_node = next_node.nextnode

        prev_node.nextnode=another_list.head

    def check_for_cycle(self):
        next_node=self.head
        next_next_node=self.head
        while(next_next_node and next_next_node.nextnode):
            next_node=next_node.nextnode
            next_next_node=next_next_node.nextnode.nextnode
            if(next_node==next_next_node):
                next_node=self.head
                while(next_node!=next_next_node):
                    next_node=next_node.nextnode
                    next_next_node=next_next_node.nextnode
                return next_node

        return False


    def remove(self,k):
        slow=self.head
        fast=self.head
        prev=self.head
        while(k):
            fast=fast.nextnode
            k=k-1
        while(fast):
            prev=slow
            slow=slow.nextnode
            fast=fast.nextnode

        prev.nextnode=slow.nextnode



    def middle_of_list(self):
        next_node = self.head
        prev_node = self.head
        index=0
        while (next_node):
            prev_node = next_node
            next_node = next_node.nextnode.nextnode
            index=index+1
        return (prev_node,index)

    def check_palindramocity(self):
        list=[]
        middle,index=self.middle_of_list()
        next_node = self.head
        for i in range(index):
            list.append(next_node.data)
            next_node=next_node.nextnode
        for i in range(index):
            data=list.pop()
            if(data!=middle.data):
                return False
            middle=middle.nextnode

        return True

    def clone(self,next_node):
        if(next_node==None):
            return None
        result=node(next_node.data)
        result.nextnode=self.clone(next_node.nextnode)
        return result



L=LinkedList(1)
print L
L.insert(6)
L.insert(2)
L.insert(3)
L.insert(5)
print L
node1=L.delete(2)
print L.randomacess(3)
L.append(8)
print L

L2=LinkedList(5)
L2.insert(11)
L2.insert(12)
L2.insert(13)
L2.insert(15)
print L
print L2
L.merge_two_lists(L2)
print L

L3=LinkedList(1)
L3.insert(2)
L3.insert(2)
L3.insert(1)

print L3.check_palindramocity()

print L3.check_for_cycle()
L3.remove(1)
print L3



