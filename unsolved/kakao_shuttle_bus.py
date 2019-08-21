# kakao_shuttle_bus
# in progress...
def solution(n, t, m, timetable):
    waiting,answer = [],9*60
    timetable = sorted([int(s[:2])*60+int(s[3:]) for s in timetable])
    bus_time = 9*60
    for _ in range(n):        
        on_board = len([ppl for ppl in timetable if ppl <= bus_time])
        if on_board > m : on_board = m
        timetable = timetable[on_board:]
        if timetable == []:
            break
        bus_time += t  
    return str(bus_time//60) + ':' + str(bus_time%60)    


if __name__ == "__main__":
    n,t,m,timetable =2,10,2,['09:10', '09:09', '08:00']	
    print(solution(n,t,m,timetable))
