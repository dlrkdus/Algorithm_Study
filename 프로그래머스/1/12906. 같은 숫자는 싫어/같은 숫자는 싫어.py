def solution(arr):
    answer = []
    i = 0
    while i < len(arr) - 1:
        if arr[i] != arr[i + 1]:
            answer.append(arr[i])
        i += 1

        if i == len(arr) - 1:
            answer.append(arr[i])

    return answer