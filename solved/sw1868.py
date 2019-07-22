#sw expert academy 1868 lv4 dfs
dy = [-1,-1,-1,0,0,0,1,1,1]
dx = [-1,0,1,-1,0,1,-1,0,1]

def printGraph(w,n) :
    print('')
    for i in range(n+2):
        for j in range(n+2):
            print(w[i][j], end = '')
        print('')

def checkZero(w,n):
    for i in range(1,n+1):
        for j in range(1, n+1):
            isZero = True
            for k in range(9):
                y = i + dy[k]
                x = j + dx[k]
                if w[y][x] == '*' : 
                    isZero = False 
                    break
            if isZero:
                w[i][j] = '0'

def clickZero(w,n,y,x):
    w[y][x] = 'X'
    for k in range(9):
        ny = y + dy[k]
        nx = x + dx[k]
        if w[ny][nx] == '0' :
            clickZero(w,n,ny,nx)
        elif w[ny][nx] == '.' :
            w[ny][nx] = 'X'

tc = int(input())
for tc in range(1, tc+1):
    n = int(input())
    w = [['~' for x in range(n+3)] for y in range(n+3)]
    for i in range(1,n+1):
        s = list(input())
        for j in range(1, n+1):
            w[i][j] = s[j-1]
    checkZero(w,n)
    #printGraph(w,n)
    click = 0 
    while(True):
        found = False
        for i in range(1, n+1):
            for j in range(1, n+1):
                if w[i][j] == '.' :
                    found = True
                    break
        if not found : break 

        for i in range(n+1):
            for j in range(n+1):
                if w[i][j] == '0' :
                    clickZero(w,n,i,j)
                    click += 1
                    #printGraph(w,n)
        for i in range(n+1):
            for j in range(n+1):
                if w[i][j] == '.':
                    click += 1
                    #printGraph(w,n)
                    w[i][j] = 'X'

    print('#%d %d' % (tc, click))


'''
2
3
..*
..*
**.
5
..*..
..*..
.*..*
.*...
.*...
'''
