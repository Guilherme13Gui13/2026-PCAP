m = []
p = input().split()
c = input().split()
p = int(p)
c = int(c)
m.append(p)
m.append(c)
m.sort()
a = len(m)
for i in range(1, m+2):
    print