N = int(input())
s = ""
count = 1
x = 0

while x < N:
    current = ""
    for a in range(count):
        current += "y"

    for b in range(count):
        current += "Y"
    count += 1
    current += s
    s += current
    if len(s) >= N:
        break

print(s[:N])

