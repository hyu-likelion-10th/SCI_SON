def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        a = participant.pop()
        if  a != completion.pop():
            return a
    return participant.pop()