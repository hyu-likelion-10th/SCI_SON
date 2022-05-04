cnt = int(input())
for i in range(cnt):
    inp = input().split()
    inp = list(map(int, inp))
    num = inp.pop(0)
    avg = sum(inp) / num
    temp_cnt = 0
    for j in inp:
        if j > avg:
            temp_cnt += 1

    print("{:.3f}%".format(temp_cnt/num * 100))