# 일단 P를 기준으로 정렬하고, 세그먼트 트리 혹은 펜윅트리를 이용해야 함은 알았다.
# 일단 구간합의 개념으로 풀 수 있으면, 펜윅트리가 더 간단하고 효율적이다.
# 사다리 타리와 순열복원에서 사용했던, 수열의 위치를 0 또는 1로 초기화한 후 구간합의 개념으로 풀 수 있을 것인가!?

# 생각 끝에 알아냈다! 단계를 나누면, 3개로 이루어진 순서쌍은 2개로 앞에 나온 수들 중, 자신보다 작은 증가하는 2개 쌍의 개수이지 않은가!?
# 따라서 각 수열의 값이 갖는 범위인 0~1000000을 각 leaf node로 2개의 펜윅 트리를 구성하고 0으로 초기화한다.
# Q를 앞에서부터 차례로 순회하면서 값 q[i] + 1의 index 위치를 1을 더해준다. (tree는 1 위치부터 시작하는데, 값은 0부터 시작하므로)
# tree_double에서 q[i] + 1 위치의 값은 tree에서 q[i]까지의 누적합(처음부터의 구간합) 값을 저장해 준다.
# 이는 q[i]보다 작으면서 수열에서 보다 앞에 나온 개수, 즉 q[i]로 끝나는 현재까지의 증가하는 2개 원소로 구성된 순서쌍의 개수를 의미한다.
# 그리고 q[i]까지의 tree_double 의 누적합은 현재 순회하고 있는 위치의 q[i]로 끝나는 증가하는 3개 원소로 구성된 순서쌍 개수가 된다.
# 따라서 Q를 순회하며 각각으로 끝나는 3개 순서쌍의 개수를 계속 더해주면, 원하는  P,Q의 유사 트리플의 개수를 얻을 수 있다!!

# 하지만 중복처리는!? p는 같은 수인데, 정렬 상 앞뒤 차이가 생겨서, q에서 증가할 때, 트리플 개수로 잘봇 추가되는 경우!
# p가 같은 구간에서 q를 순회할 때 자신보다 더 작은 수가 앞에 나와서 트리플 개수로 추가하지 않도록 
# 1. 작은 수면 다시 그 개수만큼 빼준다. or
# 2. python의 정렬시 첫 수가 같은 경우 다음 수를 기준으로 세부 정렬해주므로, 이를 이용하여 q는 역순으로 정렬하면! p가 같은데, q를 증가하는 구간으로 셀 일이 없다! p가 같을 때, q는 감소구간이 되므로.

# 펜윅트리의 누적합(구간합 query)과 update 함수
def cumulative_sum(index, tree): # 처음부터 index까지의 누적합을 계산하는 함수
    Sum = 0 # 누적합을 저장하는 변수
    while index > 0: # tree의 index는 1 ~ N
        Sum += tree[index] # 차례로 더해주면 처음부터 index까지의 누적합
        index -= index & -index # 'index & -index'는 1이 존재하는 최하위 비트를 찾아준다. index에 이것을 빼줘가면, 누적합을 위한 인덱스를 차례로 찾을 수 있다.
    return Sum

def update(index, value, tree): # 해당 위치(index)에 기존 값과의 변화랑 value를 update해 준다. 해당 index가 포함된 구간합들도 update해 준다.
    while index < len(tree): # tree의 index는 1 ~ N
        tree[index] += value # 변화된 값에 따른 구간합 갱신
        index += index & -index # index에 1이 존재하는 최하위 비트를 더해가면, 영향을 끼치는 구간합들의 index들을 탐색할 수 있다.

def solve(q, n, tree, tree_double):
    count = 0
    # last = (p[0][0] + 1) % 1000000
    # overlap = 0
    # temp = []
    for i in range(n):
        count += cumulative_sum(q[i], tree_double) # q[i]로 끝나는 트리플 개수를 Q를 순회하며 계속 더해주면 된다! DP느낌.
        # q[i]까지의 구간합.
        # overlap = 0
        # if p[i][0] == last:
        #     for num in temp:
        #         if q[i] > num:
        #             overlap += 1
        #     temp.append(q[i])
        # else:
        #     temp = [q[i]]
        update(q[i] + 1, 1, tree) # tree index는 1부터 위치하므로, 0부터 존재하는 수를 맞추기 위해 + 1, leaf는 해당 수의 개수, 누적합은 2길이 증가쌍의 개수
        update(q[i] + 1, cumulative_sum(q[i], tree), tree_double) # leaf는 해당 수로 끝나는 2길이 증가쌍의 개수의 개수, 누적합은 3길이 증가쌍의 개수
        # last = p[i][0]
    return count
        
tree = [0] * 1000002 # tree : leaf는 나온 위치의 수 0 ~ 10^6 를 1로 조정하는 펜윅트리, 누적합은 q[i]보다 작은 수의 개수. -> 2길이 증가쌍의 개수
tree_double = [0] * 1000002 # tree_double : leaf는 현재까지 검사한 q 수열에서 q[i]로 끝나는 2길이 증가쌍의 개수, q[i]보다 작은 누적합은 2길이 증가쌍의 개수 -> 3길이 증가쌍의 개수!

n = int(input())
# p = [[int(x), i] for i, x in enumerate(input().split())]
p = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]
PQ = []
Q = []
# p.sort()
# for i in range(n):
#     Q.append(q[p[i].pop()])

for i in range(n):
    PQ.append([p[i], -q[i]]) # p[i]가 같은 수인데, q[i]가 증가한다고 증가쌍의 개수를 더 세면 안된다! 
    # 그렇다면 P가 같은 구간에서 Q를 기준으로 더 작은 수가 앞에 오면 안된다. 그렇다면 Q는 역순으로 정렬하면 된다!!
PQ.sort()
for i in range(n):
    Q.append(-PQ[i][1]) # 정렬을 위해 음수처리해준 Q를 원상복귀!

print(solve(Q, n, tree, tree_double))

# 그동안 감사했습니다!! 덕분에 알고리즘 실력이 많이 늘고, Hufs Code Festival도 우승할 수 있었습니다! 정말 감사합니다^^