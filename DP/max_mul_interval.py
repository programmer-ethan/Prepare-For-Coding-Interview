# 시간복잡도 최악의 경우 O(n)의 알고리즘
# 2개의 1차원 DP를 n만큼 순회하며 차례로 완성해간다.
# 곱의 경우 양수 음수가 바뀌기 때문에, 최대합구간의 방식 그대로 사용할 수 없다.
# 결국 절댓값이 크고 양수여야 하므로.
# A[i]로 끝나는 구간 최솟값과 최댓값을 이용한다.
# 최솟값은 음의 방향으로 절댓값이 가장 큰 값을 나타내기 때문.

# 결과적으로
# A[i]가 음수일 때, A[i-1] 까지의 구간 최솟값과 곱하여 절댓값이 가장 큰 양수, 즉 최대 구간 곱이 될 경우를 고려해주면
# A[i]로 끝나는 최대, 최소 구간합은 A[i], A[i]*Max[i-1], A[i]*Min[i-1] 세가지 값을 비교하여 얻을 수 있다.
# 이렇게 구한 DP: Max를 순회하며 최대값을 return해주면, 그 값이 최대 구간 곱이다.
# n개의 정수를 한번씩 순회하면 되므로 시간복잡도 O(n)
# T(n) = 3n + 5


def max_mul_interval(A):
	n = len(A)
	Max = [0]*n # A[i]로 끝나는 최대 곱 구간
	Min = [0]*n # A[i]로 끝나는 최소 곱 구간
	Max[0] = Min[0] = A[0] # 초깃값
	for i in range(1,n):
		Min[i] = min(A[i], A[i]*Max[i-1], A[i]*Min[i-1]) # 자기자신, 자기자신*이전 최댓값, 자기자신*이전 최솟값 중 최솟값
		Max[i] = max(A[i], A[i]*Max[i-1], A[i]*Min[i-1]) # 자기자신, 자기자신*이전 최댓값, 자기자신*이전 최솟값 중 최댓값
	return max(Max) % 123464239 # DP에 저장된 값중 최대값

A = list(map(int, input().split()))
print(max_mul_interval(A))