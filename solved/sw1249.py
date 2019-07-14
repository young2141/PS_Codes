MAX = 987654321
t = int(input())

def dijkstra(n,w,m):
	ni,nj = 0,0
	for k in range(n * n):
		small = MAX
		for i in range(n):
			for j in range(n):
				if m[i][j] != -1 and m[i][j] < small :
					small = m[i][j]
					ni,nj = i,j
		if ni == n-1 and nj== n-1 :
			return m[ni][nj]

		if ni+1 < n and m[ni+1][nj] == MAX and m[ni+1][nj]  != -1:
			m[ni+1][nj] = m[ni][nj] + w[ni+1][nj]
		if nj+1 < n and m[ni][nj+1] == MAX and m[ni][nj+1] != -1:
			m[ni][nj+1] = m[ni][nj] + w[ni][nj+1]
		if ni > 0 and m[ni-1][nj] == MAX and m[ni-1][nj] != -1:
			m[ni-1][nj] = m[ni][nj] + w[ni-1][nj]
		if nj > 0 and m[ni][nj-1] == MAX and m[ni][nj-1] != -1:
			m[ni][nj-1] = m[ni][nj] + w[ni][nj-1]

		m[ni][nj] = -1
		'''
		print(ni,nj)
		for u in range(n):
			print(m[u])
		print()
		'''
	return -1


for tc in range(1, t+1):
	n = int(input())
	w = [[int(x) for x in list(input()) ]for q in range(n)]
	m = [[MAX]*n for y in range(n)]
	m[0][0] = w[0][0]

	print('#%d %d' % (tc,dijkstra(n,w,m)))

'''
2
4
0100
1110
1011
1010
6
011001
010100
010011
101001
010101
111010
'''
