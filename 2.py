s1 = input()
s2 = input()
last = s2[-1]
count = 0
n = len(s1)
for i in range(n):
    if s1[i] == last:
        count += 1
print(count)