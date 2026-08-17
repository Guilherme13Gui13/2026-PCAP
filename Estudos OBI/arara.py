N, M = input().split()
N = int(N)
M = int(M)
a = (M + 4) // 5
if a >= N*M:
    print("S")
else:
    print("N")