a=[2,5,6,9,1,2,3,5]
b = [4,2,5,7,9,1,2,15,123]

# binary search
def binary_search(num_list,target):
    new_numlist = []
    for idx,i in enumerate(num_list):
        new_numlist.append((i,idx))
    new_numlist= sorted(new_numlist,key = lambda x: x[0])
    end = len(new_numlist)-1
    start = 0
    while True:
        mid = (start+end)//2
        if start>end:
            break
        if new_numlist[mid][0] == target:
            return new_numlist[mid][1]
        elif new_numlist[mid][0]<target:
            start = mid+1
        elif new_numlist[mid][0]>target:
            end = mid-1

print(binary_search(a,3))
print(binary_search(b,5))