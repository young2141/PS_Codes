# sw academy 3752
# code looked up 
s = set()

''' time exceeded '''''' 
def recursion(arr, index, size, sumed) :
	if index == size :
		s.add(sumed)
		return
	recursion(arr,index+1, size, sumed + arr[index])
	recursion(arr, index+1, size, sumed)
'''


test_case = int(input())
for test_num in range(1, test_case+1):
	s.clear()
	n = int(input())
	number = list(map(int, input().split()))
	add_up = sum(number)
	d = [False] * (add_up+10)
	d[0] = True

	for i in range(n):
		for j in range(add_up, -1, -1):
			if d[j]:
				d[j+number[i]] = True
	answer = 0
	for i in d:
		if i:
			answer += 1
	print("#%d %d" % (test_num, answer))

'''
2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1	
'''
