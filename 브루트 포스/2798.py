N, M = map(int,input().split())
nums = list(map(int,input().split()))
max=0
for i in range(N-2): #3중 for문 돌면서 겹치지 않게 탐색
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = nums[i]+nums[j]+nums[k]
            if(sum<=M and sum>max):
                max=sum
print(max)