case_count = int(input())
for _ in range(case_count):
    student_list = list(map(int, input().split()))
    score_sum = 0
    list_len = len(student_list)
    for i in range(list_len):
        if i == list_len-1:
            break
        score_sum += student_list[i+1]
    average = score_sum/student_list[0]
    average_count = 0
    for j in range(list_len):
        if j == list_len-1:
            break
        if student_list[j+1] > average:
            average_count += 1
    result = round(average_count/student_list[0]*100, 3)
    print(format(result, ".3f")+"%")
