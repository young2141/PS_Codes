import itertools
n,m = map(int, input().split())
v = list(map(int, input().split()))
v.sort()
per = itertools.permutations(v,m)
answer = set()
for p in per:
    answer.add(p)
    
answer = list(answer)        
answer.sort()
for ans in answer:
    for a in ans:
        print(a,end= ' ')
    print()