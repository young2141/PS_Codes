# kakao_nbase_game
# in progress...

def solution(msg):
    dic,answer = list('0ABCDEFGHIJKLMNOPQRSTUVWXYZ'),[]
    
    while len(msg) > 2:
        out = False
        for i in range(len(msg)-1,-1,-1):
            for j in range(len(dic)-1,-1,-1):
                if dic[j] == msg[:i]:
                    dic.append(msg[:i+1])                    
                    msg = msg[i:]
                    answer.append(j)
                    out = True
                    break
            if out : break
        print(msg, dic[27:])    

    return answer
    
if __name__ == "__main__":
    msg = 'ABABABABABABABAB'    
    # msg = 'ABABABABABABABAB'
    print(solution(msg))

      
