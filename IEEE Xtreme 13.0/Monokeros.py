# 100% correct
def jumpSearch(inputList, number, jump):
    lowerIndex, upperIndex = 0, 0
    length = len(inputList)
    if length % jump == 0:
        start = jump - 1
    else:
        start = length % jump - 1
    for x in range(start, length, jump):
        upperIndex = x
        if inputList[lowerIndex] < number <= inputList[upperIndex]:
            break
        else:
            lowerIndex = upperIndex

    for y in range(lowerIndex, upperIndex+1):
        if number <= inputList[y]:
            return y

N = int(input())
seq = input().strip().split(" ")

seq = list(map(int, seq))
numbers = [-10**9, 10**9]
depths = [0, 0]
output = []

for num in seq:
    y = jumpSearch(numbers, num, 300)
    depth = max(depths[y-1], depths[y]) + 1
    output.append(depth)
    depths.insert(y, depth)
    numbers.insert(y, num)

print(*output)
