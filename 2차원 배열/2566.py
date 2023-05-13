m = [[int(l) for l in input().split()] for l in range(9)]
ans = m[0][0]
x = 0
y = 0

for i in range(9):
    for j in range(9):
        if ans < m[i][j]:
            ans = m[i][j]
            x = j
            y = i
print(ans)
print(y, x)