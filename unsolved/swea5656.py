# sw expert academy 5656 dfs bfs
import pprint
MAX = 987654321
answer = MAX

def dfs(w, row, col, throw, throws):
        global answer
        if throws == throw:
                count = 0
                for block in w:
                        if block != 0:
                                count += 1
                answer = min(answer, count)
                return
        
        for j in range(col):
                y,x = -1,-1
                fakew = w[:]
                for i in range(row):
                        if w[i][j] != 0 :
                                y,x = i,j
                                break
                else : y,x = 0, j            
                
                tmp = chain(fakew,y,x,w[y][x],row,col)[:]
                tmp = slide(tmp,row,col)
                pprint.pprint(w)
                print(w is tmp)
                input('pause')
                
                if j == 2:
                        print('ball num:'+str(throws),'col:'+str(j))
                        pprint.pprint(tmp)
                
                dfs(tmp,row,col,throw, throws+1)


                
def chain(w,i,j,ranges,row,col):
        q = [[i,j,ranges-1]]

        while q != []:
                y,x,ranges = map(int,q[0])
                q = q[1:]
                w[y][x] = 0                
                
                for ny in range(y-ranges, y+ranges+1):
                        for nx in range(x-ranges, x+ranges+1):
                                if ny<0 or ny>=row or nx<0 or nx>=col: continue
                                q.append([ny,nx,w[ny][nx]-1])

        return w        
                                
def slide(w,row,col):
        for j in range(col):
                tmp = []
                for i in range(row):
                        if w[i][j] != 0:
                                tmp.append(w[i][j])
                for i in range(row - len(tmp)):
                        tmp.insert(0,0)
                for i in range(row):
                        w[i][j] = tmp[i]
        return w          


tc = int(input())
for tc in range(1, tc+1):
        throw, col, row = map(int, input().split())
        w = [[int(x) for x in input().split()] for y in range(row)]

        dfs(w,row,col,throw,0)

        print('#{} {}'.format(tc, answer))
        answer = MAX
    
'''
1
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1
'''
