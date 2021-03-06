# 알고리즘 설명
# 필요한 최소의 막대개수는 삽입 또는 버블 정렬의 swap 횟수이다.
# 하지만 이를 구현하면, O(n^2)으로 100,000의 수에서는 시간초과가 나온다.
# 따라서 특별한 자료구조가 필요하다. 세그먼트 트리로도 구현할 수 있겠지만, 
# 구간합을 이용하여 풀 수 있는 문제이므로, 더 효율적인 자료구조인 펜윅 트리(Fenwick Tree, Binary Indexed Tree, BIT)를 이용하였다. 
# (tree의 메모리를 N + 1만 사용한다.)
# tree의 .각 값은 앞에서 뒤로 스쳐 지나가는데 필요한 최소 swap 횟수를 의미한다.
# 따라서 처음에는 0으로 초기화된 값을 그대로 두며, tree의 init()은 필요 없다
# 입력을 뒤에서부터 하나씩 살피며, 해당 index까지의 구간합을 구해주고
# update를 통해 값이 정해진 위치를 +1 로 갱신해준다.
# 모든 배열을 확인하며, 나온 구간합을 더하면, 필요한 최소 가로막대 수가 나온다.

# 수행시간
# 최악의 경우 O(nlog2n)의 수행시간을 갖는다.
# 입력 리스트를 탐색하면서 O(n)
# 구간합을 구하고, cumulative_sum(), 업데이트 하는데, update()
# 각각 O(log2n)이기 때문이다.

def cumulative_sum(index): # 처음부터 index까지의 누적합을 계산하는 함수
    Sum = 0 # 누적합을 저장하는 변수
    while index > 0: # tree의 index는 1 ~ N
        Sum += tree[index] # 차례로 더해주면 처음부터 index까지의 누적합
        index -= index & -index # 'index & -index'는 1이 존재하는 최하위 비트를 찾아준다. index에 이것을 빼줘가면, 누적합을 위한 인덱스를 차례로 찾을 수 있다.
    return Sum

def update(index, value): # 해당 위치(index)에 기존 값과의 변화랑 value를 update해 준다. 해당 index가 포함된 구간합들도 update해 준다.
    while index < len(tree): # tree의 index는 1 ~ N
        tree[index] += value # 변화된 값에 따른 구간합 갱신
        index += index & -index # index에 1이 존재하는 최하위 비트를 더해가면, 영향을 끼치는 구간합들의 index들을 탐색할 수 있다.

count = 0 # 필요한 가로 막대의 최소 수 = 즉 정렬의 swap 수
data = [int(x) for x in input().split()]
N = len(data)
tree = [0] * (N + 1) # tree의 index는 1 ~ N 
for i in range(N, 0, -1): # 뒤에서부터 수가 해당위치까지 뒤로 이동하는 데 필요한 swap 수.
    count += cumulative_sum(data[i - 1]) # 구간합을 계산하면서, 자신보다 원래 뒤에 있던 수가 자신의 앞의 제자리를 찾아갔으면, 
    # 그 해당 수는 tree에서 1로 바뀌어 있을 것이고, 따라서 구간합을 구하면서 count + 1된다. 즉 해당 두 수는 최소 1번 서로 swap되어야 한다는 의미. 왜냐하면 정렬과정에서 서로 반드시 지나쳐야되기 때문.
    update(data[i - 1], 1) # 구간합을 구한 후, 값을 갱신해준다. swqp count가 양쪽 수 입장에서 두번 계산되는 것을 막기 위함. 
    # 1로 갱신해주는 이유는, 스쳐지나가는데 필요한 swap count가 0에서 1로 갱신됨을 의미
print(count)

# O(n^2) 풀이 방법: 시간초과
# def bubbleSort(A):
#     n = len(A)
#     count = 0
#     for i in range(n):
#         for j in range(n - i - 1):
#             if A[j] > A[j + 1]:
#                 A[j], A[j + 1] = A[j + 1], A[j]
#                 count += 1
#     return count

# data = [int(x) for x in input().split()]
# print(bubbleSort(data))