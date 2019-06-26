n = int(input())

for i in range(1, n+1):
    s = str(i)
    count = 0
    for j in range(0,len(s)):
        if s[j] == '3' or s[j] == '9' or s[j] == '6':
            count += 1
    if count == 0 :
        print("%s "%s, end='')
    else :
        for j in range (0, count):
            print("-", end='')
    print(" ", end='')


