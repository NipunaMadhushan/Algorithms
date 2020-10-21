# 100% Correct
N, A, B = map(int, input().strip().split())

if N < A:
    print("NO")
else:
    if N <= B:
        print("YES")
        print(N)
    else:
        if N < 2*A:
            print("NO")
        else:
            if N % B == 0:
                List = [B for i in range(int(N/B))]
                print("YES")
                print(*List)
            else:
                count = int(N/B)
                if N < (count+1)*A:
                    print("NO")
                else:
                    N = N - count*B
                    List = [B for j in range(count)]

                    if N >= A:
                        List.insert(0, N)
                        print("YES")
                        print(*List)
                    else:
                        diff = A - N
                        a = 0
                        while diff > 0:
                            if diff >= B-A:
                                List[a] = A
                                diff -= B-A
                            else:
                                List[a] -= diff
                                diff = 0
                            a += 1

                        List.insert(0, A)
                        print("YES")
                        print(*List)



