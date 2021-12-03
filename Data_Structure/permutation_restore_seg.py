# 세그먼트 트리 자료구조를 이용
# 오른쪽에 확정되어 저장되는 값들로 세그먼트 트리를 업데이트(update)하며, A[i] 값을 얻는다.(query)
# 물론 B[i] + 1 에서 시작한다.
# 세그먼트 트리의 Leaf 노드의 번호 0 ~ n - 1 은 1 ~ n의 값에 대응된다. 
# 초기에 1로 초기화하며, 이미 나온 값은 0으로 update한다.
# non-leaf 노드는 자손 leaf 노드 중 아직 확정되지 않은 [오른쪽에 등장하지 않은] 수의 개수를 의미한다.
# B[n - 1]에서 시작하여 B[0]까지 차례로 A[n - 1]에서 A[0]까지 결정해 준다.
# A[i] 값을 정해주기 위해서 B[i] + 1의 값에서 시작하여 [최소의 수], 
# 세그먼트 트리의 루트에서 시작하여 방문하는 노드마다 값을 -1해주고, 어떤 값인지 찾아간다.
import math

def init(start, end, index): # 세그먼트 트리 생성
	global tree
	if start == end:
		tree[index] = 1 # leaf 노드는 1로 초기화
		return tree[index]
	mid = ( start + end ) // 2
	tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index *2 + 1) # 자손 leaf 노드 중 아직 확정되지 않은[오른쪽에 등장하지 않은] 수의 개수
	return tree[index]

def update_query(start, end, index, value):
	global tree
	tree[index] -= 1 # 자식 노드 둘 중 하나를 선택할 것이므로 -1
	if start == end: # 찾은 위치는 A[i]의 값 - 1
		return end
	mid = (start + end) // 2
	left_val = tree[index * 2] # value 값을 기준으로 어디를 찾을지 결정
	if left_val >= value: # 왼쪽 값이 value 값보다 크거나 같으면, 왼쪽을 탐색
		return update_query(start, mid, index * 2, value)
	else:
		return update_query(mid + 1, end, index * 2 + 1, value - left_val) # 왼쪽 값이 value 값보다 작으면, 오른쪽을 탐색. 왼쪽에 아직 나오지 않은 작은 값들을 value에서 빼줘야 함. 

def reconstruct(B):
	# B로부터 A를 재구성해 리턴
	global n
	A = [0] * n
	for i in range(n - 1, -1, -1): # 뒤에서 부터 하나씩 확정해 갈 수 있다. O(nlog2n)
		A[i] = update_query(0, n - 1, 1, B[i] + 1) + 1 # index가 0부터 이므로, 값을 나타내도록 + 1
	return A

B = [int(x) for x in input().split()]
n = len(B)
tree = [0] * (2 ** (1 + int(math.ceil(math.log2(n)))))
init(0, n - 1, 1)

A = reconstruct(B)
for x in A:
	print(x, end = ' ')

# 1. 본인이 작성한 알고리즘의 수행시간을 간략히 분석해보자
# init()의 경우 T(n) = 3n
# reconstruct()의 경우 T(n) = 2 + 3 * n + n * (6 * log2n)[update_query]
# 따라서 총 수행시간은 T(n) = 6 * n * log2n + 6 * n + 2

# 2. 수행시간 T(n)을 Big-O료 표기해보자
# O(n*log2n)

# 결국 0으로 바꿔주는 것의 의미는 자기보다 작은 것이 오른쪽에 나온 것을 알려주기 위해서.
# index 찾아 가는 것은, 왼쪽 1의 개수 세기