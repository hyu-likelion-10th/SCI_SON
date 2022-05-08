def solution(participant, completion):  # 효율성 검사 통과
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
