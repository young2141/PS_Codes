def solution(prices):
    stack = []
    ret = []
    for i in range(len(prices)):
        if i == 0:
            stack.append(prices[i])


if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))
