def generate_subsets_lexographical(list1):
    for i in range(2**len(list1)):
        subset=[]
        x=bin(i)[2:]
        for index,j in enumerate(reversed(x)):
            if(j=='1'):
                subset.append(list1[int(index)])

        print subset

generate_subsets_lexographical([1,2,3,4,5,6,7,8,9,10])










