# sw expert academy 7088 
# no way to grade 

tc = int(input())
for tc in range(1, tc+1):
    n, q = map(int,input().split())
    arr = [[0,0,0]]
    for i in range(n):
        spe = int(input())
        new = [arr[i][0], arr[i][1], arr[i][2]]
        new[spe-1] += 1
        arr.append(new)
    #print(arr)    
    
    for i in range(q):
        s, e = map(int, input().split())
        answer = [arr[e][0] - arr[s-1][0],
                arr[e][1] - arr[s-1][1],
                arr[e][2] - arr[s-1][2]]
        #print(answer)
    

'''
1
6 3
2
1
1
3
2
1
1 6
3 3
2 4
'''
