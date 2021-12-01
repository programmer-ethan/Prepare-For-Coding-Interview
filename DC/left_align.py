def min_penalty(width,sentences):
	n = len(sentences)
	word_length = [] # 각 단어의 길이
	for word in sentences: 
		word_length.append(len(word)) # 단어의 내용은 의미X, 단어의 길이만 사용
	min_penalties = [0] * (n + 1) # DP! i번째 단어로 끝나는 최소 패널티
	for i in range(n): # 단어 하나씩 순회
		blank = width # 현재 줄의 공백, 최대로 초기화
		cur_min_penalty = n*width**3 # 현재 최소 패널티, 최대로 초기화
		reverse_idx = i # 역순으로 단어를 검사하며, 최소 패널티를 찾기 위함
		while reverse_idx > -1: # 첫 단어까지
			blank -= word_length[reverse_idx] + 1 # 공백은 해당 단어의 길이 + 1(공백)만큼 줄어든다.
			# 새로운 줄을 만들어서 역순으로 단어 추가해가며 패널티 구해보기, 한 줄을 구성하는 것을 전부 새로 만들어볼 때까지.(그 줄에 그대로 추가하는 경우가 그 광정에서 자동으로 계산 된다.)
			penalty = min_penalties[reverse_idx] + (blank + 1) ** 3  # 새로운 패널티 계산, 마지막 공백 한칸은 패널티에 포함해서 계산
			if blank + 1 >= 0: # 공백 있으면
				cur_min_penalty = min(cur_min_penalty, penalty) # 더 최솟값 갱신 시도
			else: # 공백 없으면, 따라서 최대 w에 비례해서 반복된다. 최악의 경우도 w/2(한 글자 단어만으로 구성)번
				break # 단어를 추가할 때마다 최적의 해를 구해왔다면, 최적의 해를 찾을 때, 이전 줄만 검토하면 되기 때문!
			reverse_idx -= 1
		min_penalties[i + 1] = cur_min_penalty # DP에 갱신된 패널티 저장
	return min_penalties[n] # 마지막 최소 패널티
	
W = int(input())
sentences = input().split()
print(min_penalty(W,sentences))

# 최악의 경우 수행시간 : O(nW) 단어 순회하며, 한줄 만큼 검사(W)
# W는 상수 취급 할 수 있으므로 O(n)
# 우선 단어를 구성하는 문자개수만 필요하므로, word_length list를 만든다.
# 한 단어씩 추가해가며 (O(n)) 최소 penalty를 계산하고 DP에 저장한다.
# DP[i]는 i번째 단어로 끝나는 최소 패널티
# 이때 고려해야 할 것은, 해당 줄에서 W를 추가하면 다음줄을 추가해 주어야 하는데, 항상 최소 penalty를 갖기 위해서는, 다음 줄이 추가될 때, 기존에 위에 있던 단어도 밑으로 넘겨야 할 경우가 있다는 것.
# 항상 최소 penalty를 DP에 저장하므로, 추가되는 줄과, 그 이전 줄만 조사하면 된다.
# (이때 추가로 소요되는 수행시간은 한글자로 구성된 단어만 들어오는 최악의 경우 O(W/2), 
# 평균적으로 O(W/m) m은 '단어의 길이의 평균 + 1' )
# 따라서 수행시간은 O(nW) 혹은 O(n)
# 이때 조사하는 방법은, 일단 새 단어와 함께 항상 새 줄을 만든다고 가정하고 
# 이전 줄의 단어를 하나씩 새로 만든 줄에 가져오며 최소 패널티이면 DP 갱신, 이때 이전에 저장된 DP값 활용

# DP[i] = min(DP[j] + penalty, DP[i]) [∑(j=i부터 j--)(word_length[i] + 1) < W 인 동안]
# penalty는 새로 만든 줄의 penalty