
import math
def min_SS(B,n,F):
    sum_of_squared_deviation = [[0] * n for _ in range(n)]
    sum_of_square = [[0] * n for _ in range(n)]
    sum_of_interval = [[0] * n for _ in range(n)]
    for i in range(n):
        sum_of_interval[i][i] = F[i]
        sum_of_square[i][i] = F[i]**2
        for j in range(i + 1,n):
            sum_of_interval[i][j] = sum_of_interval[i][j] + F[j]
            sum_of_square[i][j] = sum_of_square[i][j - 1] + F[j]**2
            sum_of_squared_deviation[i][j] = sum_of_square[i][j] - sum_of_interval[i][j] ** 2  / (j - i + 1)
    
    DP = [[math.inf] * (B + 1 ) for _ in range(n + 1)] # DP[i][j]는 i개 그룹으로 나뉜 idx j번째까지의 수에 대한 최소 편차 제곱합
    for b in range(1, B + 1):
        DP[0][b] = 0
    for i in range(n):
        DP[i][0] = 0
    for i in range(1,n):
        for b in range(1,B + 1):
            if i < b:
                DP[i][b] = 0
            else:  
                for k in range(b-1, i):
                    DP[i][b] = min(DP[i][b], DP[k][b-1] + sum_of_squared_deviation[k][i])
    return DP[n-1][B]

B, n = map(int, input().split())
F = [int(input()) for _ in range(n)]
if B >= n: print(0)
else:
    print(min_SS(B,n,F))