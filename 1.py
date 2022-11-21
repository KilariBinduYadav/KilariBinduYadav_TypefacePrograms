def convertTernary(n):
    s = ""
    while n:
        r = n % 3
        n = n // 3
        s += str(r)
    return s[::-1]

n = int(input())
ter = convertTernary(n)
print(ter)