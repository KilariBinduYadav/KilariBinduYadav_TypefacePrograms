r,c = map(int, input().split())
mat = []
for i in range(r):
    row = list(map(int, input().split()))
    mat.append(row)
#print(mat)
r_set = set()
c_set = set()
for i in range(r):
    for j in range(c):
        if mat[i][j] == 0:
            r_set.add(i)
            c_set.add(j)
            break
#print(r_set,c_set)
f1 = min(r_set)
f2 = min(c_set)

r_set = set()
c_set = set()
for i in range(r):
    for j in range(c-1,-1,-1):
        if mat[i][j] == 0:
            r_set.add(i)
            c_set.add(j)
            break

l1 = max(r_set)
l2 = max(c_set)

res = [(f1,f2), (f1,l2), (l1,f2), (l1,l2)]

print(*res)
