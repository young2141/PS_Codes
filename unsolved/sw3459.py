# sw expert academy 3459
# looked up in internet

# alice = odd,0 , bob = even,1.
# choosing number : 2^depths <= n < 2^(depths+1)

import math

'''when       n 
bob           1 
alice      2       3
bob      4  5      6   7
alice  8 9 10 11  12 13 14 15  
'''
test_case = int(input())
for tc in range(1, test_case+1):

    n = int(input())
    answer = 0; x = 1;
    if n > 3:
        turn = int(math.log(n, 2))
        if turn % 2 == 0: person = 'Bob'
        else:  person = 'Alice'

        if person == 'Alice':
            for i in range(turn):
                if i % 2 == 0:
                    x = x * 2
                else: x = x * 2 + 1
            if x > n : answer = 'Bob'
            else : answer = 'Alice'
        else :
            for i in range(turn):
                if i % 2 == 0:
                    x = x * 2 + 1
                else: x = x * 2
            if x > n : answer = 'Alice'
            else : answer = 'Bob'

    else:
        if n == 1: answer = 'Bob'
        else: answer = 'Alice'

    print('#%d %s' % (tc, answer))


'''
5
1  
5   
7  
10 
123456789123456789 
'''
