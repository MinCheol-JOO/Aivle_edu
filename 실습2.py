tmp =[]
while True:
    a= input()
    if a == 'e':
        break
    tmp.append(int(a))
    tmp = sorted(tmp,reverse=True)
    print(tmp)