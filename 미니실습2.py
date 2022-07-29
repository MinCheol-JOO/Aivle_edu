# 자료구조
# 1번 시도
# a= [2,5,1,3,9,6,7]
# b = []
# for i in reversed(a):
#     b.append(i)
# print(b)

# 2번 시도
# for i in range(len(a)//2):
#     a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
#     print(a)
# print(a)

# 미니 실습 2
# a= []
# n = int(input())
# for _ in range(n):
#     b = int(input())
#     a.append(b)

# for j in range(1,len(a)+1):
#     print(f'리스트를 역으로 출력합니다 : a[-j]는 {a[-j]}')

def sentinel(num_list):
    num_list.append(3)
    return 2

num_list = [2,3]
print(num_list)
sentinel(num_list)
print(num_list)