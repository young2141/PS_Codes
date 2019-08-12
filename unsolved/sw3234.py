#sw expert academy 3234 lv4
#in progress
import itertools
answer = 0
def check(p,index,left,right,n):
        try:
                global answer              
                if left < right : return   
                if index == n :
                        answer += 1
                        #print(answer, left, right, p)
                        return
                
                
                check(p, index+1, left+p[index], right,n)
                check(p, index+1, left, right+p[index],n)

        except Exception:
                print('error' + str(index))
                print(Exception)
                return
                                

tc = int(input())
for tc in range(1, tc+1):
        n = int(input())
        numbers = [int(x) for x in input().split()]

        perm = itertools.permutations(numbers)
        for p in perm:
                check(p,0,0,0,n)
        
        print('#{} {}'.format(tc, answer))
        answer = 0

'''
3
3
1 2 4
3
1 2 3
9
1 2 3 5 6 4 7 8 9
'''
