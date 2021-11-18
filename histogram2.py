import math
def solve(B,n,F):
    # 0. 다음 평균과의 차이     1.  원소 개수      2. 그룹 합계     3. 그룹 평균
    # 3. 그룹의 원소들!
    # 5. 그룹 원소들의 평균과의 편차
    #그룹들. 초깃값은 각각을 원소로 하는 n개의 그룹. B개가 될 때까지 합친다.
    group = [ [ abs(F[i+1] - F[i]), 1, F[i], F[i] ,[F[i]], [0] ] for i in range(n - 1)]
    group.append([max(F), 1, F[n - 1], F[n - 1], [F[n - 1]], [0] ])
    for i in range(n-1, B - 1, -1): 
        # 다음 평균과의 차이가 가장 적은 위치를 고른다. 합치기 위해서
        Min_diff = max(F)
        Min_idx = 0
        group_N = len(group)
        for i in range(group_N):
            if Min_diff > group[i][0]:
                Min_diff = group[i][0]
                Min_idx = i
        # pop해서 그룹 합치기
        popped_group = group.pop(Min_idx + 1)
        past_mean = group[Min_idx][3] # 합치기 전 그룹 평균
        right_past_mean = popped_group[3] # 우측 합칠 그룹(pop한 그룹)의 이전 평듄

        
        if Min_idx >= i - 1:
            next_mean = math.inf
        else: 
            next_mean = group[Min_idx + 1][2] / group[Min_idx + 1][1] # 새로운 다음 그룹의 평균
        group[Min_idx][1] += popped_group[1] # 새 원소 개수
        group[Min_idx][2] += popped_group[2] # 새 그룹 합계  
        group[Min_idx][3] = group[Min_idx][2] / group[Min_idx][1] # 새 그룹 평균  
        group[Min_idx][0] = abs(next_mean - group[Min_idx][3])# 새 다음 평균과의 차이
        group[Min_idx][4] += popped_group[4] # 그룹 원소 추가

        # 그룹 원소들의 평균과의 편차
        for i in range(len(group[Min_idx][5])): # 합치기 전 원소들에 대해서
            group[Min_idx][5][i] += past_mean - group[Min_idx][3]
        for i in range(popped_group[1]): # pop 합 원소들에 대해서
            group[Min_idx][5].append(popped_group[5][i] + right_past_mean - group[Min_idx][3])
        
        # 이제 새로 합쳐진 그룹이 최적인지 확인.
        # 새 그룹의 원소를 뒤 그룹에 줘보는 경우
        if Min_idx < i - 1: # 마지막 그룹이 아니면
            Min_SS = 0# 최소 편차 제곱합
            for i in range(group[Min_idx][1]):
                Min_SS += group[Min_idx][5][i]**2
            for i in range(group[Min_idx + 1][1]):
                Min_SS += group[Min_idx + 1][5][i]**2    
            # 하나 pop
            popped_num = group[Min_idx][4].pop()
            group[Min_idx][5].pop()
            group[Min_idx][1] -= 1
            group[Min_idx][2] -= popped_num
            group[Min_idx][3] = group[Min_idx][2] / group[Min_idx][1]
            # pop합 것 다음 그룹에 넣기
        # 현재편차 제곱합

        # i는 현 상태 그룹 개수
        #if Min_idx < i - 1: # 마지막 그룹이 아니면

        # 1개의 원소를 앞으로 옮기고 혹시 편차 제곱합이 더 작으면 유지하고, 다음 확인.
    # 편차 제곱 합 구하기
    SS = 0
    for each_group in group:
        for deviation in each_group[5]:
            SS += deviation**2    
    return round(SS, 3)

B, n = map(int, input().split())

F = [int(input()) for _ in range(n)]
if B >= n: print(0)
else:
    print(solve(B,n,F))