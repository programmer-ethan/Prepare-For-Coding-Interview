# 분산의 특징을 활용한 방법 Try
# 편차제곱합을  (제곱의 평균 - 평균의 제곱) * n으로 구할 수 있다.
import math
def min_SS(B,n,F):
    # DP식으로 최소 제곱을 구하려면
    # i ~ j의 오차식을 구해두는 것이 편하다. (위의 공식 활용
    # i~j의 개수는 알 수 있으므로
    # i ~ j의 합을 통해 평균을 구할 수 있다.
    # 제곱의 평균은 n이 곱해져  i~j 구간 제곱의 합을 구한다.
    # 나머지 매트릭스 반은 사용하지 않는다.
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
    
    DP = [[0] * n for _ in range(B + 1)] # DP[i][j]는 i개 그룹으로 나뉜 idx j번째까지의 수에 대한 최소 편차 제곱합
    for j in range(n):
        DP[1][j] = sum_of_squared_deviation[0][j]
    for i in range(1, B + 1):
        DP[i][0] = 0
    for i in range(2, B + 1):
        Min_SS = math.inf
        for j in range(1,n):
            cur_SS = sum_of_squared_deviation[j][n-1] + DP[i - 1][j - 1]
            Min_SS = min(Min_SS, cur_SS)
        DP[i][j] = Min_SS
    return DP[B][n - 1]

B, n = map(int, input().split())
F = [int(input()) for _ in range(n)]
if B >= n: print(0)
else:
    print(min_SS(B,n,F))