# sw expert academy 1486 lv4 subset

answer = 987654321

def subset(h,i,B,l):
	global answer
	if i == len(h):
		if l >= B and answer > l :
			answer = l
		return

	subset(h,i+1, B, l+h[i])
	subset(h,i+1, B, l)


tc = int(input())
for tc in range(1, tc+1):
	N,B = map(int,input().split())
	h = [int(x) for x in list(input().split())]

	subset(h, 0, B,0)
	print('#%d %d' % (tc, answer - B))
	answer = 987654321
'''
1
3 120
83 64 36
'''
