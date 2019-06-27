n = int(input())

for i in range(0,n):
	s  = input()
	now = (int(s[0]) * 10 + int(s[1]))* 60 * 60 + (int(s[3])*10 + int(s[4]))*60 + int(s[6])*10 + int(s[7])
	s = input()
	goal = (int(s[0]) * 10 + int(s[1]))* 60 * 60 + (int(s[3])*10 + int(s[4]))*60 + int(s[6])*10 + int(s[7])
	answer = 0

	if goal > now :
		answer = goal - now
	else:
		answer = (24 * 60 * 60 - now) - goal
	hour = answer // (60*60)
	minute = (answer - hour * 60 * 60) // 60
	sec = answer - hour*60*60 - minute*60
	print("#%d %02d:%02d:%02d\n"%(i+1, hour,minute,sec))
