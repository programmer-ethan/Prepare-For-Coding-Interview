# A[i] = n - L[i] - (i - S[i])
# A[i] = n - 오른쪽에 있는 자신보다 큰 수의 개수(L[i]) - 왼쪽에 있는 자신보다 큰 수의 개수(i - S[i])
def reconstruct(S, L):
	n = len(S)
	A = []
	for i in range(n):
		A.append(n - L[i] + S[i] - i) # A[i] = n - L[i] - (i - S[i])
		# 즉 A[i]는 오른쪽에 있는 자신보다 큰 수의 개수(L[i])와 왼쪽에 있는 자신보다 큰 수의 개수(i - S[i])를 위 식과 같이 확정할 수 있다.
	return A

# S와 L을 차례로 읽어들임
S = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
A = reconstruct(S,L)
for x in A:
	print(x, end = ' ')

# 1. 본인이 작성한 알고리즘의 수행시간을 간략히 분석해보자
# T(n) = 6n + 2 핵심 알고리즘은 한줄이지만, 산술연산, 복사연산 등의 기본 연산에 의해서
# A[i] 하나 만드는데, 산술연산 3개, 복사연산 2개, append 1개, 따라서 6n

# 2. 수행시간 T(n)을 Big-O료 표기해보자
# O(n) = n
# 수행시간이 6n + 2 이므로, 최악의 경우에도 n에 비례하는 알고리즘이다.
# 따라서 O(n) = n, 최고차항에 따라 정해지므로.