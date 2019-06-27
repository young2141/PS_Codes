#Runtime error (maximum recursion)
test_size = int(input())
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def check(s,y,x):
	if len(s) == 7:
		if visit[int(s)] == 0 :
			visit[int(s)] = 1
			return 1
		else:
			return 0
	else :
		for i in range(4):
			newy = y + dy[i]
			newx = x + dx[i]
			if(newy <0 or newy >= 4 or newx <0 or newx >= 4): continue
			s += str(w[newy][newx])
			check(s,newy,newx)

for test_num in range(1, test_size+1):
	visit = [0] * 10000000
	w = [[int(x) for x in input().split()] for y in range(4)]
	answer = 0
	for i in range(4):
		for j in range(4):
			answer += check("",i,j)
	print("#%d %d"%(test_num, answer))

'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
'''
