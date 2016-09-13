
import random

def construct_candidates(solution,input1):
    candidates=[]
    for i in input1:
        if i not in solution:
            candidates.append(i)

    return candidates

def permute_list(solution,input1):
    if(len(solution)==len(input1)):
        print solution
    else:
        candidates=construct_candidates(solution,input1)
        for i in candidates:
            solution.append(i)
            permute_list(solution,input1)
            solution.pop()


def random_permutation(input1):

    for i in range(len(input1)-2):
        j=random.randrange(0,len(input1)-i)
        input1[i],input1[i+j]=swap(input1[i],input1[i+j])
    print input1

def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def generate_next_permutation(input1):
    increasing_index=len(input1)-1
    while(increasing_index):
        if(input1[increasing_index-1]>input1[increasing_index]):
            increasing_index=increasing_index-1
        else:
            break
    increasing_index=increasing_index-1
    next_high=input1[increasing_index+1]
    index1=increasing_index+1
    for index,element in enumerate(input1[increasing_index+1:]):
        if(element<next_high and element>input1[increasing_index]):
            next_high=element
            index1=increasing_index+1+index
    input1[increasing_index],input1[index1]=swap(input1[increasing_index],input1[index1])
    for index,i in enumerate(reversed(input1[increasing_index+1:])):
        input1[increasing_index+1+index]=i

    return input1





print generate_next_permutation([5,4,1,2,3])






