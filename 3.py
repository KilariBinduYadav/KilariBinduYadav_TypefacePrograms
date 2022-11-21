lcd = ['1','2','5','6','8','9']
temp = lcd[:6]
n = int(input())
if n <= len(lcd):
    print(lcd[n-1])
else:
    val = 10
    while n > len(lcd):
        s = str(val)
        f = 1
        for j in range(len(s)):
            if s[j] not in temp and s[j] != '0':
                f = 0
                break
        if f:
            lcd.append(val)
        val += 1
    #print(lcd)            
    print(lcd[n-1])