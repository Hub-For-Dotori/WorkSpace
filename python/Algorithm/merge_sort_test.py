i = [1,3,6,7,9,11,14]
j = [2,4,5,8,10,12,13]
g = []

q = 0
z = 0


for p in range(len(i)+len(j)):
    if z >= len(j) or q >= len(i):
        break
    else :
        print("q : ",q)
        print("z : ",z)
        if i[q] < j[z]:
            g.append(i[q])
            q = q + 1
        else:
            g.append(j[z])
            z = z + 1
    print(g)    
