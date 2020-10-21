# 100% correct
K, J = map(int, input().strip().split())

minimum = min(K, J)
maximum = (K+J) // 3
count = min(minimum, maximum)

print(count)
