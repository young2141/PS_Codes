#wrong answer... for some reason... 
test_size = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visit = set()


def check(s, y, x, m):
	if len(s) == 7:
		visit.add(s)
		return
	for ii in range(4):
		newy = y + dy[ii]
		newx = x + dx[ii]
		if newy < 0 or newy >= 4 or newx < 0 or newx >= 4: continue
		check(s+str(m[newy][newx]), newy, newx, m)


for test_num in range(1, test_size+1):
	w = [[int(x) for x in input().split()] for y in range(4)]
	answer = 0
	for i in range(4):
		for j in range(4):
			check("", i, j, w)
	answer = len(visit)
	#print(visit)
	print("#%d %d"%(test_num, answer))

'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
'''
