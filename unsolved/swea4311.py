# no library allowed... 

def calc(a,b,op):
    a,b = int(a), int(b)
    if op == '1': 
        if a+b <= 999 : return a+b 
    elif op == '2': 
        if a-b >= 0 : return a-b 
    elif op == '3': 
        if a*b <= 999 : return a*b
    elif op == '4': 
        if b : return a//b    
    return -1

tc = int(input())
for tc in range(1, tc+1):
    n,o,max_hit = map(int, input().split())
    numbers = input().split()
    ops = input().split()
    goal = input()
    answer = 987654321
    tester = list(goal)
    for t in tester:
        if t not in numbers: break
    else: answer = len(goal)
    
    visit = [0 for _ in range(1000)]    
    q = [['', 0]]
    
    while q:
        s,cnt = q[0]
        q = q[1:]
        if cnt > max_hit : continue
        
        if s == goal:
            answer = min(answer, cnt+1)
            continue

        candi = [[s,cnt]]
        if len(s) <3 :
            for num in numbers:
                candi.append([s+num,cnt+1])
        for cn,cc in candi:
            if cn == '': continue
            cn = int(cn)
            
            num = ''           
                        

                num = int(num)
                for op in ops:
                    result =  calc(cn,num,op)
                    if result != -1:
                        if visit[result] == 0 or visit[result] > cc +2:
                            visit[result] = cc+2
                            q.append([str(result), cc+2])
                            
    if answer == 987654321: answer = -1
    print('#%d %d'%(tc, answer))
                
            
        