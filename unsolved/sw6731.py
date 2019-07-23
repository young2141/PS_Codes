#sw expert academy 6731 lv4 bfs(brute-force)

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def printGraph(w,n):
        print()
        for i in range(n):
                for j in range(n): 
                        print(w[i][j], end ='')
                print()

def coloring(w,n,i,j):
        for x in range(n):
                w[i][x] = w[i][x] * -1
        for y in range(n):
                w[y][j] = w[y][j]* -1
        w[i][j] = w[i][j] * -1
def uncolor(w,n,i,j):
        for x in range(n):
                w[i][x] = w[i][x] * -1
        for y in range(n):
                w[y][j] = w[y][j]* -1
        w[i][j] = w[i][j] * -1
                        

def search(w,g,n,c):
        if c >= n*n :
                return 0

        for i in range(n):
                for j in range(n):
                        coloring(g,n,i,j)
                        if w==g : return c
                        c = search(w,g,n,c+1)
                        uncolor(g,n,i,j)
        return 0             

tc = int(input())
for tc in range(1,tc+1):
    n = int(input())
    w = [[1]*n for i in range(n)]
    g = [[1]*n for i in range(n)]

    for i in range(n):
        s = list(input())
        for j, color in enumerate(s):
                if color =='W':
                        w[i][j] = 1
                else :
                        w[i][j] = -1
    printGraph(w,n)
    if w != g :
        answer = search(w,g,n,0)
    else: answer = 0
    print('#%d %d' % (tc, answer))


'''
4
4
WWWW
WWWW
WWWW
WWWW
4
WBWW
WBWW
BBBB
WBWW
4
BWWB
WWBB
WBWB
BBBW
4
WBWB
WBWB
WBWB
WBWB
'''
