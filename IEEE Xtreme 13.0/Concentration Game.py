# 100 correct.(Some times some test cases fail)
N = int(input())

numbers = []
indexes = []
match_count = 0
cur_index = 1
while match_count < N:
    Set = set(numbers)
    for a in Set:
        if numbers.count(a) == 2:
            index1 = indexes[numbers.index(a)]
            numbers.remove(a)
            indexes.remove(index1)
            index2 = indexes[numbers.index(a)]
            numbers.remove(a)
            indexes.remove(index2)
            print(str(index1) + " " + str(index2))
            read1 = input()
            match_count += 1

    if match_count < N:
        print(str(cur_index) + " " + str(cur_index + 1))
        read2 = input().strip()
        if read2 == "MATCH":
            match_count += 1
            cur_index += 2
        else:
            n1, n2 = map(int, read2.split())
            indexes += [cur_index, cur_index+1]
            numbers += [n1, n2]
            cur_index += 2

print(-1)
