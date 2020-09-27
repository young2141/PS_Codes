def solution(participant, completion):

    runner = {}

    for p in participant:
        if p in runner.keys():
            runner[p] = runner[p] + 1
        else:
            runner[p] = 1

    for c in completion:
        if not c in runner.keys():
            return c
        elif runner[c] == 1:
            del runner[c]
        elif runner[c] >= 2:
            runner[c] = runner[c] - 1

    for key, value in runner.items():
        if value == 1:
            return key


if __name__ == "__main__":
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(solution(participant, completion))
