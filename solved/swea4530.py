# sw expert academy 4530 lv4

def calc(num):
	ret = 0
	l = len(str(num))
	n = str(num)
	s = 0
	for i in range(l-1, -1, -1):
		val = int(n[i])
		if val > 4 :
			val -= 1
		ret += val * pow(9,s)
		s += 1
	return  ret - 1

tc = int(input())
for tc in range(1, tc+1):
	start, end = map(int,input().split())
	if start <0 and end > 0 :
		answer = calc(abs(start)) + calc(abs(end)) + 1
	else:
		answer = calc(abs(end)) - calc(abs(start))


	print('#{} {}'.format(tc, abs(answer)))

'''
4
1 1
5 10 
-3 -5
-2 -1
'''


