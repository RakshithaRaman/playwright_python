lines = ["apple", "banana", "cherry"]

result = {i+1: line for i, line in enumerate(lines)}

print(result)


def replace_zeros(arr):
    result = []
    count = 0

    for num in arr:
        if num == 0:
            count += 1
        else:
            if count > 0:
                result.append(f"{count}x0")
                count = 0
            result.append(num)

    if count > 0:
        result.append(f"{count}x0")

    return result


arr = [1,2,3,0,0,0,2,4,5,0,0,0,0,3,4,8,0,0,1]
print(replace_zeros(arr))


def find_missing_fib(arr):
    for i in range(len(arr)-1):
        if arr[i] + arr[i+1] != arr[i+2]:
            return arr[i] + arr[i+1]

arr = [1, 1, 2, 3, 5, 8, 21, 34]
print(find_missing_fib(arr))  # 8


d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 2, "c": 3, "d": 2}

result = {}

for k in d1:
    if k not in d2 or d1[k] != d2[k]:
        result[k] = d1[k]

for k in d2:
    if k not in d1:
        result[k] = d2[k]

print(result)