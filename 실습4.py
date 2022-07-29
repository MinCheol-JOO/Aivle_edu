a = [9,2,3,4,1,1,5]
b = [2,4,5,5,6,1,1,2]
def max_idx(num_list):
    tmp =[]
    for idx,i in enumerate(num_list):
        tmp.append((i,idx))
        
    tmp = sorted(tmp,key = lambda x: x[0])
    return tmp[-1][1]

print(max_idx(a))
print(max_idx(b))