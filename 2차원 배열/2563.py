판때기 = [[0 for i in range(101)] for _ in range(101)]
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    # 입력끝..
    # 풀이
    # 10x10영역을 1로 채운다.
    # 시작좌표. y, x
    for i in range(10):
        판때기[y+i][x:x+10] = [1] * 10

ans = 0  # 1이 몇번 나왔는지 저장할 변수

for x in range(1, 101):
    for y in range(1, 101):
        if 판때기[y][x] == 1:
            ans += 1
print(ans)