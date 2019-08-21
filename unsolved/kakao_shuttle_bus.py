# kakao_shuttle_bus
# in progres...

def solution(n, t, m, timetable):
    waiting,answer = [],90*60
    timetable = sorted([int(s[:2])*60+int(s[3:]) for s in timetable])
    bus_time = 90*60
    for _ in range(n):        
        on_board = len([ppl for ppl in waiting if ppl <= bus_time])
        if on_board > m : on_board = m
        waiting = waiting[m:]
        if waiting == []:
            break
        bus_time += t  
    
    


if __name__ == "__main__":
    n,t,m,timetable = 1,1,5,["08:00", "08:01", "08:02", "08:03"]
    print(solution(n,t,m,timetable))
