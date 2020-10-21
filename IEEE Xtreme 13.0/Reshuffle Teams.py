def addCount(rMem, aMem, team):
    if rMem == team:
        if aMem == team:
            return 0
        else:
            return -1
    else:
        if aMem == team:
            return 1
        else:
            return 0


def noOfCounts(S, members, team):
    length = len(S)
    count = S[:members].count(team)
    countList = [count]
    for x in range(1, length):
        rMem = S[(x-1) % length]
        aMem = S[(members+(x-1)) % length]
        count += addCount(rMem, aMem, team)
        countList.append(count)

    return countList


def minimumChange(S):
    List = [k1 for k1 in S]
    length = len(S)
    teams = ["A", "B", "C", "D"]
    no_members = []
    for i in range(4):
        num = List.count(teams[i])
        no_members.append(num)

    orders = [[0, 1, 2, 3],
              [0, 2, 1, 3],
              [0, 1, 3, 2],
              [0, 3, 1, 2],
              [0, 2, 3, 1],
              [0, 3, 2, 1]]

    countListA = noOfCounts(List, no_members[0], teams[0])
    countListB = noOfCounts(List, no_members[1], teams[1])
    countListC = noOfCounts(List, no_members[2], teams[2])
    countListD = noOfCounts(List, no_members[3], teams[3])
    countList = [countListA, countListB, countListC, countListD]

    minimum = length
    for order in orders:
        firstL = 0
        secondL = firstL + no_members[order[0]]
        thirdL = secondL + no_members[order[1]]
        fourthL = thirdL + no_members[order[2]]

        for x in range(length):
            countList1 = countList[order[0]]
            count1 = countList1[(firstL+x) % length]
            countList2 = countList[order[1]]
            count2 = countList2[(secondL+x) % length]
            countList3 = countList[order[2]]
            count3 = countList3[(thirdL+x) % length]
            countList4 = countList[order[3]]
            count4 = countList4[(fourthL+x) % length]

            total = length - (count1 + count2 + count3 + count4)

            if total < minimum:
                minimum = total

    return minimum


T = int(input())

output = []
for t in range(T):
    S = input()
    minimum = minimumChange(S)
    output.append(minimum)

for p in output:
    print(p)

