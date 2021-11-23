# O(n^2)으로 
# n개의 그룹에서 시작해서 B개의 그룹이 될 때까지 
# 그룹 평균의 차이가 작은 그룹끼리 합쳐가며 계산하는 방식
import math
import copy
def solve(B,n,F):
    # 0. 다음 평균과의 차이     1.  원소 개수      2. 그룹 합계     3. 그룹 평균
    # 3. 그룹의 원소들!
    # 5. 그룹 원소들의 평균과의 편차
    #그룹들. 초깃값은 각각을 원소로 하는 n개의 그룹. B개가 될 때까지 합친다.
    group = [ [ abs(F[i+1] - F[i]), 1, F[i], F[i] ,[F[i]], [0] ] for i in range(n - 1)]
    group.append([max(F), 1, F[n - 1], F[n - 1], [F[n - 1]], [0] ])
    for x in range(n-1, B - 1, -1): 
        # 다음 평균과의 차이가 가장 적은 위치를 고른다. 합치기 위해서
        Min_diff = math.inf
        Min_idx = 0
        group_N = len(group)
        for i in range(group_N):
            if Min_diff > group[i][0]:
                Min_diff = group[i][0]
                Min_idx = i
        #print("Min_idx:",Min_idx)
        # pop해서 그룹 합치기
        popped_group = group.pop(Min_idx + 1)
        past_mean = group[Min_idx][3] # 합치기 전 그룹 평균
        right_past_mean = popped_group[3] # 우측 합칠 그룹(pop한 그룹)의 이전 평듄
        if Min_idx >= x - 1:
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
        # x는 현 상태 그룹 개수
        if Min_idx < x - 1: # 마지막 그룹이 아니고 다음 그룹이 1개가 아니면
            Min_SS = 0# 최소 편차 제곱합
            for i in range(group[Min_idx][1]):
                Min_SS += group[Min_idx][5][i]**2
            for i in range(group[Min_idx + 1][1]):
                Min_SS += group[Min_idx + 1][5][i]**2  
            #print("group[Min_idx]:",group[Min_idx])
            while group[Min_idx][1] > 1:
                recover1 = copy.deepcopy(group[Min_idx]) # 복원용 값 저장
                recover2 = copy.deepcopy(group[Min_idx + 1]) 
                # 하나 pop하고 해당 그룹 값들 갱싱
                past_mean2 = group[Min_idx][3]
                popped_num = group[Min_idx][4].pop()
                group[Min_idx][5].pop()
                group[Min_idx][1] -= 1
                group[Min_idx][2] -= popped_num
                group[Min_idx][3] = group[Min_idx][2] / group[Min_idx][1]
                for i in range(len(group[Min_idx][5])): # 새로운 편차 계산
                    group[Min_idx][5][i] += past_mean2 - group[Min_idx][3]
                # pop합 것 다음 그룹에 넣기
                past_mean3 = group[Min_idx + 1][3]
                group[Min_idx + 1][4].insert(0, popped_num)
                group[Min_idx + 1][1] += 1
                group[Min_idx + 1][2] += popped_num
                group[Min_idx + 1][3] = group[Min_idx + 1][2] / group[Min_idx + 1][1]
                group[Min_idx + 1][5].insert(0, popped_num - group[Min_idx + 1][3])
                for i in range(1, len(group[Min_idx + 1][5])): # 새로운 편차 계산
                    group[Min_idx + 1][5][i] += past_mean3 - group[Min_idx + 1][3]
                cur_SS= 0
                for i in range(group[Min_idx][1]):
                    cur_SS += group[Min_idx][5][i]**2
                for i in range(group[Min_idx + 1][1]):
                    cur_SS += group[Min_idx + 1][5][i]**2
                if cur_SS < Min_SS: # 최소 값이 바뀌면 갱신
                    #print("최소 값이 바뀌면 갱신")
                    Min_SS = cur_SS
                else: # 못 바꾸면 원상복귀
                    #print("못 바꾸면 원상복귀")
                    group[Min_idx] = recover1
                    group[Min_idx + 1] = recover2
                    break
                #print("recover1:",recover1)

        # 1개의 원소를 앞으로 옮기고 혹시 편차 제곱합이 더 작으면 유지하고, 다음 확인
        if Min_idx > 0:
            Min_SS = 0# 최소 편차 제곱합
            for i in range(group[Min_idx][1]):
                Min_SS += group[Min_idx][5][i]**2
            for i in range(group[Min_idx - 1][1]):
                Min_SS += group[Min_idx - 1][5][i]**2  
            
            #print("group[Min_idx]:",group[Min_idx])
            while group[Min_idx][1] > 1:
                recover1 = copy.deepcopy(group[Min_idx]) # 복원용 값 저장
                recover2 = copy.deepcopy(group[Min_idx - 1]) 
                # 하나 pop하고 해당 그룹 값들 갱싱
                past_mean2 = group[Min_idx][3]
                popped_num = group[Min_idx][4].pop(0)
                group[Min_idx][5].pop(0)
                group[Min_idx][1] -= 1
                group[Min_idx][2] -= popped_num
                group[Min_idx][3] = group[Min_idx][2] / group[Min_idx][1]
                for i in range(len(group[Min_idx][5])): # 새로운 편차 계산
                    group[Min_idx][5][i] += past_mean2 - group[Min_idx][3]
                # pop합 것 이전 그룹에 넣기
                past_mean3 = group[Min_idx - 1][3]
                group[Min_idx - 1][4].append(popped_num)
                group[Min_idx - 1][1] += 1
                group[Min_idx - 1][2] += popped_num
                group[Min_idx - 1][3] = group[Min_idx - 1][2] / group[Min_idx - 1][1]
                group[Min_idx - 1][5].append(popped_num - group[Min_idx - 1][3])
                for i in range(len(group[Min_idx - 1][5]) - 1): # 새로운 편차 계산
                    group[Min_idx - 1][5][i] += past_mean3 - group[Min_idx - 1][3]
                cur_SS= 0
                for i in range(group[Min_idx][1]):
                    cur_SS += group[Min_idx][5][i]**2
                for i in range(group[Min_idx - 1][1]):
                    cur_SS += group[Min_idx - 1][5][i]**2
                if cur_SS < Min_SS: # 최소 값이 바뀌면 갱신
                    #print("최소 값이 바뀌면 갱신")
                    Min_SS = cur_SS
                else: # 못 바꾸면 원상복귀
                    #print("못 바꾸면 원상복귀")
                    group[Min_idx] = recover1
                    group[Min_idx - 1] = recover2
                    break

    # 편차 제곱 합 구하기
    #print(group)
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