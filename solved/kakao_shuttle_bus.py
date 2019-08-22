# kakao_shuttle_bus programmers

def solution(n, t, m, timetable):

    timetable = sorted([int(s[:2])*60+int(s[3:]) for s in timetable])
    bus_time, last , last_bus = 9*60, 0, 9*60 + t*(n-1)
    
    for _ in range(1,n):
        for i in range(m):
            if len(timetable) < m and i == len(timetable): break
            if len(timetable) == 1: last = timetable[0]; break
            if timetable[i] <= bus_time: timetable = timetable[1:]
        if last != 0: break
        bus_time += t
    else: 
        if len(timetable) >= m:
            last = min(timetable[m-1] - 1, last_bus)
        else : last = bus_time
    
    return f'%02d'%(last//60) + ':' + f'%02d'%(last%60)


if __name__ == "__main__":
    n, t, m, timetable =	2, 10, 2, ["09:10", "09:09", "08:00"]
    print(solution(n, t, m, timetable))
