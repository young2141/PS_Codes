# kakao_dart_game programmers string trim
powers = {'S': 1, 'D': 2, 'T': 3}
prices = ['*', '#']


def solution(dartResult):
    i, points = 0, []
    while i < len(dartResult):
        point = int(dartResult[i])
        if dartResult[i+1].isdigit():
            point = point * 10 + int(dartResult[i+1])
            i = i + 1
        point = point ** powers[dartResult[i+1]]
        points.append(point)
        if(i+2 < len(dartResult) and dartResult[i+2] in prices):
            if dartResult[i+2] == '*':
                if len(points) >= 2:
                    points[-2] *= 2
                points[-1] *= 2
            if dartResult[i+2] == '#':
                points[-1] *= -1
            i = i + 3
        else:
            i = i+2

    print(points)
    return sum(points)


if __name__ == "__main__":
    dartResult = '1D2S3T*'
    print(solution(dartResult))
