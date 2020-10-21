# Memory Limit Exceeds
T = int(input())

output = []
for i in range(T):
    B = int(input())
    N = int(input())
    num_comp = list(map(int, input().strip().split()))
    costs = []
    minimum, maximum = 0, 0
    for j in range(N):
        comp_set = list(map(int, input().strip().split()))
        if len(comp_set) == 1:
            minimum += comp_set[0]
        else:
            comp_set.sort()
            min_num = comp_set[0]
            minimum += min_num
            comp_set = [(k - min_num) for k in comp_set[1:]]
            maximum += comp_set[-1]
            costs.append(comp_set)

    remain = B - minimum

    if remain < 0:
        output.append(0)
    else:
        if remain >= maximum:
            output.append(minimum + maximum)
        else:
            List = costs.pop(0)
            List = [r for r in List if r <= remain]
            List.insert(0, 0)
            for x in range(len(costs)):
                cost_list = [q for q in costs[x] if q <= remain]
                #cost_list = costs.pop(0)
                length = len(List)
                for y in List[:length]:
                    for z in cost_list:
                        if y+z <= remain:
                            List.append(y+z)
                        else:
                            break

            output.append(max(List) + minimum)

for p in output:
    print(p)

