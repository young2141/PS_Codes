# sw expert academy 4408, looked up

tc = int(input())
for tc in range(1, tc+1):
    n = int(input())
    students = []
    corridor = [0] * 220
    
    for _ in range(n):
        s,e = map(int, input().split())
        students.append([s,e])
    
    for i in students:
        start = (i[0] - 1)//2
        end = (i[1] - 1)//2
        start, end = min(start, end), max(start, end)
        
        for j in range(start, end+1):
            corridor[j] += 1

    answer = max(corridor)
    print('#{} {}'.format(tc, answer))

'''
3  
4  
10 20 
30 40
50 60
70 80
2 
1 3
2 200
3
10 100
20 80
30 50
'''
