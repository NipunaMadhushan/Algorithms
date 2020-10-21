# 100% correct
N, M = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
S = list(map(int, input().strip().split()))

S.sort()
index = 0
y = 0
while y < M:
    num = S[y]
    for x in range(index, len(A)):
        if num < A[x]:
            A.insert(x, num)
            index = x + 1
            break
        elif x == len(A)-1:
            A = A + S[y:]
            M = 0
            break
    y += 1

print(*A)
