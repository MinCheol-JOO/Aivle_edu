def is_prime(num):
    tmp =[2]
    
    for i in range(2,num+1):
        flag =0
        for j in range(2,i):
            if i%j==0:
                flag = 1
                break
            # if j == i-1:
            #     tmp.append(i) type 1
        if flag ==0:
            tmp.append(i)
            
           
    return tmp
print(is_prime(1000)) 
print(len(is_prime(1000)))