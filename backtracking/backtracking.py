
"""
@solution: The solution Vector That is Constructed incrementally
@parameter: Parameter for recursion
@data: Data that is used to generate solution
"""

"""
Prototype for backtracking algorithm

def backtrack(solution_array,parameter,data):

    if(is_a_solution(solution_array,parameter,data)):
        process_solution(solution_array,parameter,data)
    else:
        parameter=parameter+1
        candidates=construct_candidates(solution_array,parameter,data)
        for candidate in candidates:
            solution_array.append(candidate)
            make_move(solution_array,k,data)
            backtrack(solution_array,parameter,data)
            unmake_move(solution_array,k,data)

"""

"""
1.Generate all permutations

"""
def construct_candidates1(solution_array ,k ,data):
    bool_list=[0]* (data+1)
    for i in solution_array:
        if(i!='0'):
            bool_list[i]=1

    candidates=[]
    for index, element in enumerate(bool_list[1:]):
        if( element==0 ):
            candidates.append(index+1)
    return candidates

def is_a_solution1(solution_array, parameter,data ):
    if( parameter==data-1) :
        return True
    else:
        return False

def process_solution1(solution_array, parameter, data):
    print solution_array




def backtrack1(solution_array, parameter, data):

    if(is_a_solution1( solution_array, parameter,data)):
        process_solution1( solution_array, parameter,data)
        return
    else:
        parameter= parameter+1
        candidates= construct_candidates1(solution_array, parameter,data)
        for candidate in candidates:
            solution_array[parameter]=candidate
            backtrack1(solution_array, parameter,data)
            solution_array[parameter]='0'

def construct_candidates2(solution_array ,k ,data):
    bool_list=[0]* (data+1)
    for i in solution_array:
        if(i!='0'):
            bool_list[i]=1

    candidates=[]
    for index, element in enumerate(bool_list[1:]):
        if( element==0 and index!=k):
            candidates.append(index+1)
    return candidates



def backtrack2(solution_array, parameter, data):

    if(is_a_solution1( solution_array, parameter,data)):
        process_solution1( solution_array, parameter,data)
        return
    else:
        parameter= parameter+1
        candidates= construct_candidates2(solution_array, parameter,data)
        for candidate in candidates:
            solution_array[parameter]=candidate
            backtrack2(solution_array, parameter,data)
            solution_array[parameter]='0'


backtrack1(solution_array=['0']*3,parameter=-1,data=3)
print "done"
backtrack2(solution_array=['0']*7,parameter=-1,data=7)









