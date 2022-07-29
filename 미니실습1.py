# 미니실습 1
t= (4,7,5.6,2,3.14,1)
s = 'string'
a= ('DTS','AAC','FLAC')

def min_of(s):
    minner = s[0]
    for i in s:
        if minner>i:
            minner =i
    
    return minner

print(min_of(t))
 
print(min_of(s))

print(min_of(a))
            
        