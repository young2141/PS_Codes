test_case = int(input())
for test_number in range(1, test_case+1):
    n = int((input()))
    cost = list(map(int, input().split()))
    big, answer = -1, 0
    for i in reversed(cost):
        if big < i :
            big = i
        else :
            answer += big - i
    print("#%d %d" % (test_number, answer))
