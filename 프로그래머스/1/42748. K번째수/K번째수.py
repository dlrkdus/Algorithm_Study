def solution(array, commands):
    answer = []
    for command in commands:
        answer.append(order(array,command))
    return answer

def order(array,command):
    indexed_array = array[command[0]-1:command[1]]
    indexed_array.sort()
    return indexed_array[command[2]-1]