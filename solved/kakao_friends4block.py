# kakao_friends_4_block


def shift(m, n, w):
    for j in range(n):
        col = []
        for i in range(m):
            if w[i][j] != ' ':
                col.append(w[i][j])
        for i in range(m-len(col)):
            col.insert(0, ' ')
        for i in range(m):
            w[i][j] = col[i]


def solution(m, n, board):
    w = [list(board[m]) for m in range(m)]
    answer = 0

    while True:
        same, pop = [], False
        for i in range(m-1):
            for j in range(n-1):
                if w[i][j] != ' ' and w[i][j] == w[i+1][j] == w[i][j+1] == w[i+1][j+1]:
                    same.append([i, j])
                    same.append([i+1, j])
                    same.append([i, j+1])
                    same.append([i+1, j+1])
                    pop = True

        if pop == False:
            break
        unique = []
        for coord in same:
            if coord not in unique:
                unique.append(coord)

        for coord in unique:
            w[coord[0]][coord[1]] = ' '
            answer += 1
        shift(m, n, w)
    return answer


if __name__ == "__main__":
    m, n, board = 4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
    print(solution(m, n, board))
