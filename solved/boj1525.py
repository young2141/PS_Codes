from collections import deque
import copy
import sys
sys.stdin = open('input.txt', 'r')


def check_and_append(tmp, q, count):
    ss = ''.join(tmp)
    if ss not in visit:
        visit.add(ss)
        q.append([tmp, count+1])


def swap_right(tmp, q, count):
    tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
    check_and_append(tmp, q, count)


def swap_left(tmp, q, count):
    tmp[i], tmp[i-1] = tmp[i-1], tmp[i]
    check_and_append(tmp, q, count)


def swap_down(tmp, q, count):
    tmp[i], tmp[i+3] = tmp[i+3], tmp[i]
    check_and_append(tmp, q, count)


def swap_up(tmp, q, count):
    tmp[i], tmp[i-3] = tmp[i-3], tmp[i]
    check_and_append(tmp, q, count)


goal = '123456780'

s = []
for i in range(3):
    s += input().split()

visit = set([''.join(s)])
q = deque([[s, 0]])
answer = -1
while q:    
    s, count = q.popleft()
    if ''.join(s) == goal:
        answer = count
        break

    for i in range(9):
        if s[i] == '0':
            if i % 3 == 0:
                swap_right(s[:], q, count)
            if i % 3 == 1:
                swap_left(s[:], q, count)
                swap_right(s[:], q, count)
            if i % 3 == 2:
                swap_left(s[:], q, count)

            if i-3 >= 0:
                swap_up(s[:], q, count)
            if i+3 <= 8:
                swap_down(s[:], q, count)


print(answer)
