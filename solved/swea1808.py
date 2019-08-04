# sw expert academy 1808 lv4 dfs

answer = 987654321

def get_factor(goal):
	factor = []
	for i in range(2, goal+1):
		if goal % i == 0 :
			factor.append(i)
	factor.sort(reverse=True)
	return factor

def is_makeable(num,button):
	s = str(num)
	for i in range(len(s)):
		if not int(s[i]) in button :
			return False
	return True

def dfs(candi, i, goal,value,count):
	global answer
	if value > goal : return
	if i >= len(candi) : return
	if count >= answer : return
	if value == goal :
		answer = count
		return

	dfs(candi, i, goal, value*candi[i], count + len(str(candi[i]))+1 )
	dfs(candi, i+1, goal, value, count)
	dfs(candi, i+1, goal, value * candi[i], count + len(str(candi[i]))+1)



tc = int(input())
for tc in range(1, tc+1):

	b = map(int,input().split())
	button = []
	for i,x in enumerate(b):
		if x == 1:
			button.append(i)
	goal = int(input())
	factor = get_factor(goal)

	candi = []
	for num in factor:
		if is_makeable(num,button):
			candi.append(num)
	#print(candi)
	dfs(candi, 0,goal, 1,0)

	if answer == 987654321:
		answer = -1
	if goal == 1:
		answer = 2
	print('#%d %d' % (tc, answer))
	answer = 987654321


'''
3
0 1 1 0 0 1 0 0 0 0
60
1 1 1 1 1 1 1 1 1 1
128
0 1 0 1 0 1 0 1 0 1
128
'''
