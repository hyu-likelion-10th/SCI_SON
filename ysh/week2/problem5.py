def solution(phone_book):
    phone_book.sort(key=len)
    d = {}
    for num in phone_book:
        temp = ''
        for i in num:
            temp += i
            if temp in d:
                return False
        d[temp] = 0
    return True

print(solution(["12","123","1235","567","88"]))
print(solution(["119", "123","456","789","97674223", "1195524421"]))
print(solution(["123","456","789"]))