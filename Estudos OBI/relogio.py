H = int(input())
M = int(input())
S = int(input())
T = int(input())
H = H * 60 * 60
M = M * 60
TT = M + H + S + T
H = TT // 3600
M = (TT % 3600) // 60
S = (TT % 3600) % 60
print(H)
print(M)
print(S)