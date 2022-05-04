word = input().upper()
data = {}
for i in word:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1

print(data)

max = 0
for i in data:
    if data[i] > max:
        temp = [i]
        max = data[i]
    elif data[i] == max:
        temp.append(i)

if len(temp) >= 2:
    print("?")
else:
    print(temp[0])