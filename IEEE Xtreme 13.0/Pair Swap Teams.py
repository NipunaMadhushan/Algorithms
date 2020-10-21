# 55.56% correct. (Two TLE cases and two wrong answers)
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
    orderSet = 0
    xValue = 0
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
                orderSet = order
                xValue = x

    count = minimumPairs(List, orderSet, xValue, no_members, teams)

    return count


def minimumPairs(S, orderSet, xValue, members, teams):
    length = len(S)

    firstTeam = teams[orderSet[0]]
    secondTeam = teams[orderSet[1]]
    thirdTeam = teams[orderSet[2]]
    fourthTeam = teams[orderSet[3]]
    teams = [firstTeam, secondTeam, thirdTeam, fourthTeam]

    firstL = 0
    secondL = firstL + members[orderSet[0]]
    thirdL = secondL + members[orderSet[1]]
    fourthL = thirdL + members[orderSet[2]]
    endL = length

    if firstL+xValue < length:
        if secondL+xValue <= length:
            List1 = S[firstL+xValue:secondL+xValue]
        else:
            List1 = S[firstL+xValue:] + S[:(secondL+xValue) % length]
    else:
        List1 = S[(firstL+xValue) % length:(secondL+xValue) % length]

    if secondL+xValue < length:
        if thirdL+xValue <= length:
            List2 = S[secondL+xValue:thirdL+xValue]
        else:
            List2 = S[secondL+xValue:] + S[:(thirdL+xValue) % length]
    else:
        List2 = S[(secondL+xValue) % length:(thirdL+xValue) % length]

    if thirdL+xValue < length:
        if fourthL+xValue <= length:
            List3 = S[thirdL+xValue:fourthL+xValue]
        else:
            List3 = S[thirdL+xValue:] + S[:(fourthL+xValue) % length]
    else:
        List3 = S[(thirdL+xValue) % length:(fourthL+xValue) % length]

    if fourthL+xValue < length:
        if endL+xValue <= length:
            List4 = S[fourthL+xValue:endL+xValue]
        else:
            List4 = S[fourthL+xValue:] + S[:(endL+xValue) % length]
    else:
        List4 = S[(fourthL+xValue) % length:(endL+xValue) % length]

    List = [List1, List2, List3, List4]
    countList = []
    for y in List:
        counts = [y.count(teams[b1]) for b1 in range(4)]
        countList.append(counts)

    count = 0
    for x in range(3):
        diffList = []
        for c1 in range(4):
            if c1 != x:
                diff = countList[x][c1] - countList[c1][x]
                diffList.append(countList[x][c1] - countList[c1][x])
                countList[c1][x] = 0
                if diff < 0:
                    countList[c1][c1] += countList[x][c1]
                else:
                    countList[c1][c1] += (countList[x][c1] - diff)
                countList[x][x] += countList[x][c1]
                count += countList[x][c1]
                countList[x][c1] = 0
            else:
                diffList.append(0)

        for c2 in range(4):
            if diffList[c2] > 0:
                for c3 in range(4):
                    if diffList[c3] < 0:
                        add = diffList[c2] + diffList[c3]
                        if add <= 0:
                            countList[c3][c2] += diffList[c2]
                            diffList[c3] += diffList[c2]
                            diffList[c2] = 0
                            break
                        else:
                            countList[c3][c2] += abs(diffList[c3])
                            diffList[c2] += diffList[c3]
                            diffList[c3] = 0

    return count


T = int(input())

output = []
for t in range(T):
    S = input()
    minimum = minimumChange(S)
    output.append(minimum)

for p in output:
    print(p)


# For Testing

#S = "ABCABCBAC"
#S = "ABCABCABC"
#S = "ABDC"
#S = "ABCDABCDABCDAABDACCDABAD"
#S = "CCACACC"

#print(minimumChange(S))

#countList = [[6, 2, 1, 1], [1, 5, 1, 2], [2, 1, 5, 0], [1, 1, 1, 6]]

#count = 0
#for x in range(3):
#    diffList = []
#    for c1 in range(4):
#        if c1 != x:
#            diff = countList[x][c1] - countList[c1][x]
#            diffList.append(countList[x][c1] - countList[c1][x])
#            countList[c1][x] = 0
#            if diff < 0:
#                countList[c1][c1] += countList[x][c1]
#            else:
#                countList[c1][c1] += (countList[x][c1] - diff)
#            countList[x][x] += countList[x][c1]
#            count += countList[x][c1]
#            countList[x][c1] = 0
#        else:
#            diffList.append(0)
#
#    for c2 in range(4):
#        if diffList[c2] > 0:
#            for c3 in range(4):
#                if diffList[c3] < 0:
#                    add = diffList[c2] + diffList[c3]
#                    if add <= 0:
#                        countList[c3][c2] += diffList[c2]
#                        diffList[c3] += diffList[c2]
#                        diffList[c2] = 0
#                        break
#                    else:
#                        countList[c3][c2] += abs(diffList[c3])
#                        diffList[c2] += diffList[c3]
#                        diffList[c3] = 0

#print(count)
