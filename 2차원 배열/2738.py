ll = []
rl = []

n, m = map(int, input().split())

for _ in range(n): #좌항 입력
    t = list(map(int, input().split()))
    ll.append(t)

for l in ll: #우항 입력
    r = list(map(int, input().split()))
    for i in zip(l, r):
        print(sum(i), end=" ")
    print()