N = int(input())
first = 666 #처음 666인 수
while N != 0:# N 이 0이 아니면 계속 반복
    if '666' in str(first):
        N = N-1# N을 1 감소시키고
        if N == 0:# 만약 N 이 0이면
            break# 반복문을 탈출한다.
    first = first + 1
print(first)