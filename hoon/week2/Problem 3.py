word = input().lower()
char_unique = list(set(word))
char_list = []
char_count = []
char_dict = {}

for i in range(len(word)):
    char_list.append(word[i])
for x in char_unique:
    char_count.append(char_list.count(x))
    char_dict[x] = char_list.count(x)

char_count_unique = list(set(char_count))
sort_char_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

try:
    if sort_char_dict[0][1] != sort_char_dict[1][1]:  # 애매한 값이 중복되어도 ?가 나오는 문제 발생
        result = sort_char_dict[0][0].upper()
    else:
        result = '?'

except:  # 한글자만 있으면 발생하는 list index 에러 예외처리
    result = sort_char_dict[0][0].upper()

print(result)
