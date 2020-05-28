# This is small AI algorithm created to solve a problem in IEEE Xtreme 13.0 (Puzzle of Rooks).
# Link - https://csacademy.com/contest/ieeextreme-practice/task/puzzle-of-rooks
# Inputs - Initial positions of the rooks
# Constraints   - Rooks can be moved in x and y directions (not in diagonals)
#               - Any two rooks cannot share the same row or column
#               - Chessboard is infinitely large
#               - All the initial positions and target positions are given within the ranges 1<=x<=99 and 1<=y<=99
#Operations 1) You can move the rooks in four directions (left-L,right-R,up-U and down-D)
#           2) You can take-T(remove) one rook at a time from its current position and mark the position.
#           3) You can put-P the removed rook back to the position where you took it. But you can only take one rook out of the chess board and you should put it back before you take
#               another rook from the board.
# Task - Move the rooks from their initial position to target position.

def Move_X_Initials(N, initialCells, targetCells, xMax):
    # Rearrange rooks
    operations = []

    xIniSorted = [k1[0] for k1 in initialCells]
    xIniSorted.sort()
    xIniIndexes = []
    for p1 in xIniSorted:
        for p2 in range(N):
            if initialCells[p2][0] == p1:
                xIniIndexes.append(p2)
                break

    xTarSorted = [k2[0] for k2 in targetCells]
    xTarSorted.sort()
    xTarIndexes = []
    for p1 in xTarSorted:
        for p2 in range(N):
            if targetCells[p2][0] == p1:
                xTarIndexes.append(p2)
                break

    xIniMean = 0
    for r1 in xIniSorted:
        xIniMean += r1
    xIniMean = int(xIniMean/N)+1
    xIniMean += int(N/2)
    xTarMean = 0
    for r2 in xTarSorted:
        xTarMean += r2
    xTarMean = int(xTarMean/N)+1
    xTarMean += int(N/2)
    mean = int((xIniMean+xTarMean)/2) + 1

    value = max(N*2-2, mean)

    xAxis = [0 for i1 in range(max(value, xMax) + 1)]
    for a1 in initialCells:
        xAxis[a1[0]] = 1

    for q1 in range(N - 1, -1, -1):
        xCur = xIniSorted[q1]
        curIndex = xIniIndexes[q1]
        yCur = initialCells[curIndex][1]
        if xCur < value:
            for x1 in range(xCur, value):
                operations.append([x1, yCur, "R"])

        elif xCur > value:
            for x2 in range(xCur-1, value-1, -1):
                if xAxis[x2] == 1:
                    c = 1
                    while True:
                        if xAxis[x2-c] != 1:
                            break
                        else:
                            c += 1
                    for count in range(c-1, -1, -1):
                        operations.append([x2 - count, initialCells[xIniIndexes[q1 - count - 1]][1], "L"])
                        xAxis[x2-count] = 0
                        xAxis[x2-count-1] = 1
                        initialCells[xIniIndexes[q1 - count - 1]][0] = x2 - count - 1
                        xIniSorted[q1 - count - 1] -= 1

            for x3 in range(xCur, value, -1):
                operations.append([x3, yCur, "L"])

        xAxis[xCur] = 0
        xAxis[value] = 1
        initialCells[curIndex][0] = value
        xIniSorted[q1] = value
        value -= 2
    #print("...............Rearrange x-initials with single spaces................")
    #print("X Co-ordinates: ", xAxis)
    #print("Initial Cells: ", initialCells)
    #print("Operations: ", operations)


    # Move rooks to get order of target positions
    #operations = []     # To check

    for d in range(N):
        index = xTarIndexes[d]
        xInitial = initialCells[index][0]
        order = xIniSorted.index(xInitial)
        cIndex = xIniIndexes[order]
        yValue = initialCells[cIndex][1]
        e = order-1
        while e >= d:
            xCur1 = xIniSorted[e]
            cIndex1 = xIniIndexes[e]
            yValue1 = initialCells[cIndex1][1]
            operations.append([xCur1, yValue1, "R"])
            operations.append([xCur1+1, yValue1, "T"])
            operations.append([xCur1+2, yValue, "L"])
            operations.append([xCur1+1, yValue, "L"])
            operations.append([xCur1+1, yValue1, "P"])
            operations.append([xCur1+1, yValue1, "R"])

            xIniIndexes.remove(cIndex1)
            xIniIndexes.insert(e+1, cIndex1)
            initialCells[cIndex1][0] += 2
            initialCells[cIndex][0] -= 2
            e -= 1

    #print(".......................Rearrange x-initials with the order of targets....................")
    #print("Initial Cells: ", initialCells)
    #print("Target Cells: ", targetCells)
    #print("Operations: ", operations)

    # Move rooks to target positions
    #operations = []     # To check
    xAxis = [0 for i1 in range(max(xIniSorted[-1], xMax)+1)]
    for a2 in xIniSorted:
        xAxis[a2] = 1

    for q2 in range(N):
        xIni = xIniSorted[q2]
        fIndex = xIniIndexes[q2]
        xTar = xTarSorted[q2]
        yIni = initialCells[fIndex][1]
        if xTar < xIni:
            for x5 in range(xIni, xTar, -1):
                operations.append([x5, yIni, "L"])
        elif xTar > xIni:
            for x6 in range(xIni+1, xTar+1):
                if xAxis[x6] == 1:
                    c1 = 1
                    while True:
                        if xAxis[x6+c1] != 1:
                            break
                        else:
                            c1 += 1
                    for count in range(c1 - 1, -1, -1):
                        operations.append([x6+count, initialCells[xIniIndexes[q2+count+1]][1], "R"])
                        xAxis[x6+count] = 0
                        xAxis[x6+count+1] = 1
                        initialCells[xIniIndexes[q2+count+1]][0] = x6+count+1
                        xIniSorted[q2+count+1] += 1

            for x7 in range(xIni, xTar):
                operations.append([x7, yIni, "R"])

        xAxis[xIni] = 0
        xAxis[xTar] = 1
        initialCells[fIndex][0] = xTar
        xIniSorted[q2] = xTar

    #print(".......................Move rooks to target positions.........................")
    #print("Initial Cells: ", initialCells)
    #print("Target Cells: ", targetCells)
    #print("Operations: ", operations)

    return operations, initialCells


def Move_Y_Initials(N, initialCells, targetCells, yMax):
    # Rearrange rooks
    operations = []

    yIniSorted = [k1[1] for k1 in initialCells]
    yIniSorted.sort()
    yIniIndexes = []
    for p1 in yIniSorted:
        for p2 in range(N):
            if initialCells[p2][1] == p1:
                yIniIndexes.append(p2)
                break

    yTarSorted = [k2[1] for k2 in targetCells]
    yTarSorted.sort()
    yTarIndexes = []
    for p1 in yTarSorted:
        for p2 in range(N):
            if targetCells[p2][1] == p1:
                yTarIndexes.append(p2)
                break

    yIniMean = 0
    for r1 in yIniSorted:
        yIniMean += r1
    yIniMean = int(yIniMean/N)+1
    yIniMean += int(N/2)
    yTarMean = 0
    for r2 in yTarSorted:
        yTarMean += r2
    yTarMean = int(yTarMean/N)+1
    yTarMean += int(N/2)
    mean = int((yIniMean+yTarMean)/2) + 1

    value = max(N*2-2, mean)
    yAxis = [0 for i1 in range(max(value, yMax) + 1)]
    for a1 in initialCells:
        yAxis[a1[1]] = 1

    for q1 in range(N-1, -1, -1):
        yCur = yIniSorted[q1]
        curIndex = yIniIndexes[q1]
        xCur = initialCells[curIndex][0]
        if yCur < value:
            for y1 in range(yCur, value):
                operations.append([xCur, y1, "U"])

        elif yCur > value:
            for y2 in range(yCur-1, value-1, -1):
                if yAxis[y2] == 1:
                    c = 1
                    while True:
                        if yAxis[y2-c] != 1:
                            break
                        else:
                            c += 1
                    for count in range(c-1, -1, -1):
                        operations.append([initialCells[yIniIndexes[q1-count-1]][0], y2-count, "D"])
                        yAxis[y2-count] = 0
                        yAxis[y2-count-1] = 1
                        initialCells[yIniIndexes[q1-count-1]][1] = y2-count-1
                        yIniSorted[q1-count-1] -= 1

            for y3 in range(yCur, value, -1):
                operations.append([xCur, y3, "D"])

        yAxis[yCur] = 0
        yAxis[value] = 1
        initialCells[curIndex][1] = value
        yIniSorted[q1] = value
        value -= 2
    #print("...............Rearrange x-initials with single spaces................")
    #print("X Co-ordinates: ", xAxis)
    #print("Initial Cells: ", initialCells)
    #print("Operations: ", operations)


    # Move rooks to get order of target positions
    #operations = []     # To check

    for d in range(N):
        index = yTarIndexes[d]
        yInitial = initialCells[index][1]
        order = yIniSorted.index(yInitial)
        cIndex = yIniIndexes[order]
        xValue = initialCells[cIndex][0]
        e = order-1
        while e >= d:
            yCur1 = yIniSorted[e]
            cIndex1 = yIniIndexes[e]
            xValue1 = initialCells[cIndex1][0]
            operations.append([xValue1, yCur1, "U"])
            operations.append([xValue1, yCur1+1, "T"])
            operations.append([xValue, yCur1+2, "D"])
            operations.append([xValue, yCur1+1, "D"])
            operations.append([xValue1, yCur1+1, "P"])
            operations.append([xValue1, yCur1+1, "U"])

            yIniIndexes.remove(cIndex1)
            yIniIndexes.insert(e+1, cIndex1)
            initialCells[cIndex1][1] += 2
            initialCells[cIndex][1] -= 2
            e -= 1

    #print(".......................Rearrange x-initials with the order of targets....................")
    #print("Initial Cells: ", initialCells)
    #print("Target Cells: ", targetCells)
    #print("Operations: ", operations)

    # Move rooks to target positions
    #operations = []     # To check
    yAxis = [0 for i2 in range(max(yIniSorted[-1], yMax)+1)]
    for a2 in yIniSorted:
        yAxis[a2] = 1

    for q2 in range(N):
        yIni = yIniSorted[q2]
        fIndex = yIniIndexes[q2]
        yTar = yTarSorted[q2]
        xIni = initialCells[fIndex][0]
        if yTar < yIni:
            for y5 in range(yIni, yTar, -1):
                operations.append([xIni, y5, "D"])
        elif yTar > yIni:
            for y6 in range(yIni+1, yTar+1):
                if yAxis[y6] == 1:
                    c1 = 1
                    while True:
                        if yAxis[y6+c1] != 1:
                            break
                        else:
                            c1 += 1
                    for count in range(c1 - 1, -1, -1):
                        operations.append([initialCells[yIniIndexes[q2+count+1]][0], y6+count, "U"])
                        yAxis[y6+count] = 0
                        yAxis[y6+count+1] = 1
                        initialCells[yIniIndexes[q2+count+1]][1] = y6+count+1
                        yIniSorted[q2+count+1] += 1

            for y7 in range(yIni, yTar):
                operations.append([xIni, y7, "U"])

        yAxis[yIni] = 0
        yAxis[yTar] = 1
        initialCells[fIndex][1] = yTar
        yIniSorted[q2] = yTar

    #print(".......................Move rooks to target positions.........................")
    #print("Initial Cells: ", initialCells)
    #print("Target Cells: ", targetCells)
    #print("Operations: ", operations)

    return operations, initialCells


N = int(input())
initialCells = []
xMax, yMax = 1, 1
for n in range(N):
    a, b = map(int, input().strip().split())
    initialCells.append([a, b])
    if xMax < a:
        xMax = a
    if yMax < b:
        yMax = b

targetCells = []
for n in range(N):
    a, b = map(int, input().strip().split())
    targetCells.append([a, b])
    if xMax < a:
        xMax = a
    if yMax < b:
        yMax = b

#print("Initial Cells: ", initialCells)
operations1, initialCells = Move_X_Initials(N, initialCells, targetCells, xMax)
#print("Operations: ", operations1)
#print("Initial Cells: ", initialCells)
#print("Target Cells: ", targetCells)

operations2, initialCells = Move_Y_Initials(N, initialCells, targetCells, yMax)
#print("Operations: ", operations2)
#print("Initial Cells: ", initialCells)
#print("Target Cells: ", targetCells)

operations = operations1 + operations2

K = len(operations)
print(K)
for oper in operations:
    print(*oper)


