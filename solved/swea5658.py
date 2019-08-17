# sw expert academy 5658 sw test
passwords = set([])
def get_passwords(nums,n):
    global passwords
    while nums != [] :
        num = ''
        for i in range(0,n):
                num += nums[i]        
        passwords.add(num)
        nums = nums[n:]
        

tc = int(input())
for tc in range(1, tc+1):
    n, k = map(int, input().split())
    nums = list(input())
    get_passwords(nums, n//4)

    for _ in range(n//4 -1):    
        tmp = nums[-1]
        nums = nums[:-1]
        nums.insert(0,tmp)
        get_passwords(nums,n//4)
    
    passwords = list(passwords)   

    passwords.sort(reverse = True)
    answer = passwords[k-1]

    answer = int(answer, 16)

    print('#{} {}'.format(tc, answer))
    passwords = set([])

'''
5
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
20 14
88F611AE414A751A767B
24 16
044D3EBA6A647B2567A91D0E
28 11
8E0B7DD258D4122317E3ADBFEA99


1
12 10
1B3B3B81F75E

'''
