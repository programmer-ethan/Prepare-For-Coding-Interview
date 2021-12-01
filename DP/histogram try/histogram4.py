
import math
import sys
def min_SS(B,n,F):
    sum_of_squared_deviation = [[0] * n for _ in range(n)]
    sum_of_square = [[0] * n for _ in range(n)]
    sum_of_interval = [[0] * n for _ in range(n)]
    for i in range(n):
        sum_of_interval[i][i] = F[i]
        sum_of_square[i][i] = F[i]**2
        for j in range(i + 1,n):
            sum_of_interval[i][j] = sum_of_interval[i][j-1] + F[j]
            sum_of_square[i][j] = sum_of_square[i][j - 1] + F[j]**2
            sum_of_squared_deviation[i][j] = sum_of_square[i][j] - sum_of_interval[i][j] ** 2  / (j - i + 1)
    DP = [[math.inf] * (B + 1) for _ in range(n + 1)] # DP[i][j]는 j개 그룹으로 나뉜 idx i번째까지의 수에 대한 최소 편차 제곱합
    for b in range(1, B + 1):
        DP[0][b] = 0
    for i in range(n+1):
        DP[i][0] = 0
    for i in range(n):
        DP[i+1][1] = sum_of_squared_deviation[0][i]
    for i in range(1,n + 1):
        for b in range(2,B + 1):
            if i <= b:
                DP[i][b] = 0
            else:  
                for k in range(i//2,i):
                    #print("i: ",i," b: ",b," k: ",k)
                    #print(DP[k][b-1] + sum_of_squared_deviation[k][i-1])
                    DP[i][b] = min(DP[i][b], DP[k][b-1] + sum_of_squared_deviation[k][i-1])
    #print(DP)
    return DP[n][B]

B = int(sys.stdin.readline())
n = int(sys.stdin.readline())
F = [int(sys.stdin.readline()) for _ in range(n)]
if B >= n: print(0)
else:
    print(min_SS(B,n,F))