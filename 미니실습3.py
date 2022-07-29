a= [2,5,1,3,9,6,7]
num=10

# # 선형탐색
# import math
# idx = 0
# cnt=0
# while idx != math.inf:
#     cnt+=1
#     if cnt == len(a):
#         print(-1)
#         print(cnt)
#         break
#     if a[idx] == num:
#         print(cnt)  
    
#     idx+=1
    

# 보초법
a.append(num)
import math
cnt =0
idx=0
while a[idx] != num:
    cnt+=1
    idx+=1
if cnt == len(a)-1:
    print(-1)    
else:
    print(cnt)

import copy

# from copy import deepcopy

# a= [1,2,3]
# b =copy.deepcopy(a)
# b.append(4)
# print(a)
# print(b)