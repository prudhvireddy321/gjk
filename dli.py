#a
o = int(input())
q = [ int(x) for x in input().split()]
o = len(q)
u = 0
for i in range(0,o-2):
    for j in range(i+1, o-1):
        for k in range(j+1, o):
            if q[i] > q[j] > q[k] :
                u =u+ 1
print(u)
  
