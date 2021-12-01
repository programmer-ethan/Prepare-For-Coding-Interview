import math
def solve(B,n,F):
    # 차이가 가장 적은 것들 부터 합친다.
    # 차이를 나타내는 리스트
    # 저장되는 원소.  0.이전그룹원의 개수  1.그룹원의 개수  2.그룹원의 합  3.그룹 평균  4.다음그룹과의 차이
    # 초기화 0: 1   1:1  2:F[i]  3:F[i]  4:abs(F[i+1] - F[i])
    differences = [[1, 1, F[i], F[i], abs(F[i+1] - F[i])] for i in range(n - 1)] # 0 ~ n-2 생성 
    #print("differences:", differences)
    differences.append([1, 1, F[n - 1], F[n - 1], 0]) # differences[n-1]은 다음그룹과의 차이 사용 X
    for _ in range(n-B): # B 개의 그룹을 생성한다. n-b개를 옆평균과 차이가 적은 순서대로 병합시킨다.
        # 다음그룹과의 차이의 최솟값 뽑기
        Min_diff = max(F)
        Min_idx = 0
        idx = 0
        while idx < n - 1:
            #print("idx:",idx)
            if Min_diff > differences[idx][4]:
                Min_diff = differences[idx][4]
                Min_idx = idx
            idx += differences[idx][1]
        # 다음 그룹을 나눠가지는 것이 최선일 수도 있으므로!
        before_group_num = differences[Min_idx][1] # 좌측(현) 그룹의 그룹원 수
        next_group_num = differences[Min_idx + before_group_num][1] # 다음(중간) 그룹의 그룹원 수
        Partial_Min_SS = math.inf # 중간 그룹을 나눠 가졌을 때, 그 이후 두그룹의 최소 편차 제곱합
        right_group_idx = Min_idx + differences[Min_idx][1] + next_group_num # 다다음(우측) 그룹의 시작 인덱스
        if right_group_idx < n: # 다다음 그룹이 존재한다면
            divide_idx = Min_idx + before_group_num # 중간 그룹을 나눌 위치의 절대 인덱스
            left_group_num = differences[Min_idx][1] # 초기에는 좌측 그룹만
            left_group_sum = differences[Min_idx][2]
            right_group_num = differences[right_group_idx][1] + differences[Min_idx + before_group_num][1] # 초기에는 중간, 우측 그룹의 합
            right_group_sum = differences[right_group_idx][2] + differences[Min_idx + before_group_num][2]
            for relative_idx in range(next_group_num):
                # 좌측 그룹의 정보
                left_group_num += 1
                left_group_sum += F[Min_idx + relative_idx + 1]
                # 우측 그룹의 정보
                right_group_num -= 1
                right_group_sum -= F[Min_idx + relative_idx + 1]

                left_mean = left_group_sum / left_group_num
                right_mean = right_group_sum / right_group_num
                for + relative_idx + 1

        else:
            # 그룹 합치기
            #print("Min_idx:", Min_idx)
            #print("Min_idx + before_group_num:", Min_idx + before_group_num)
            differences[Min_idx][1] += differences[Min_idx + before_group_num][1] # 그룹원 더하기
            differences[Min_idx][2] += differences[Min_idx + before_group_num][2] # 합끼리 더하기
            
            # print("Min_idx + differences[Min_idx][1]:", Min_idx + differences[Min_idx][1])
            differences[Min_idx][3] = differences[Min_idx][2] / differences[Min_idx][1] # 새 평균 구하기
            #print("differences[Min_idx][3]:", differences[Min_idx][3])
            # 다음그룹 과의 차이 구하기
            if Min_idx + differences[Min_idx][1] < n - 1:
                differences[Min_idx][4] = abs(differences[Min_idx + differences[Min_idx][1]][3] - differences[Min_idx][3]) # 합치기 때문에 다다음 그룹 조사
                differences[Min_idx + differences[Min_idx][1]][0] = differences[Min_idx][1] # 다음 그룹에 이전 그룹원 개수 갱신
            else:
                differences[Min_idx][4] = max(F)
            #print("differences[Min_idx][4]:", differences[Min_idx][4])
            # 이전 그룹의 다음 그룹과의 차이 갱신: 첫 수의 경우 제외...
            if Min_idx != 0:
                differences[Min_idx - differences[Min_idx][0]][4] = abs(differences[Min_idx - differences[Min_idx][0]][3] - differences[Min_idx][3])
        
            
    # 편차 제곱 합 구하기
    #for i in range(n):
        #print(differences[i])
    i = 0
    SS = 0
    while i < n: #
        #print("group num -1")
        mean = differences[i][3]
        for _ in range(differences[i][1]):
            #print("(differences[i][3] - F[i]) ** 2",(differences[i][3] - F[i]) ** 2)
            SS += (mean - F[i]) ** 2
            i += 1
        #print("SS",SS)
    return round(SS, 3)

B, n = map(int, input().split())
F = [int(input()) for _ in range(n)]
if B >= n: print(0)
else:
    print(solve(B,n,F))