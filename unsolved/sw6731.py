# sw expert academy 6731 lv4 
# no way to grade it. looked up 

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def printGraph(w, n):
    print()
    for i in range(n):
        for j in range(n):
            print(w[i][j], end='')
        print()

def search(w,n):
	ret = 0
	g = [[0] * n for i in range(n)]
	for i in range(n):
		for j in range(n):
			addUp = 0 - w[i][j]
			for y in range(n):
				addUp += w[y][j]
			for x in range(n):
				addUp += w[i][x]
			g[i][j] = addUp
			if addUp % 2 == 1:
				ret += 1

	#printGraph(g,n)
	return ret

tc = int(input())
for tc in range(1, tc + 1):
    n = int(input())
    w = [[0] * n for i in range(n)]

    for i in range(n):
        s = list(input())
        for j, color in enumerate(s):
            if color == 'W':
                w[i][j] = 0
            else:
                w[i][j] = 1
    #printGraph(w, n)
    answer = search(w,n)

    print('#%d %d' % (tc, answer))

'''
4
4
WWWW
WWWW
WWWW
WWWW
4
WBWW
WBWW
BBBB
WBWW
4
BWWB
WWBB
WBWB
BBBW
4
WBWB
WBWB
WBWB
WBWB
'''
