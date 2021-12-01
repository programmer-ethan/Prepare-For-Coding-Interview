def reconstruct(B):
	# B로부터 A를 재구성해 리턴
	# 이 함수를 작성합니다~
	n=len(B)
	A=[0]*n
	C=set()#A[i]에 들어간 수의 집합
	for i in range(n-1,-1,-1):#x는 A[i]에 넣을 값.
		x=B[i]
		for y in range(1,x):#x=B[i]보다 작은 값 y가 집합 C에 있으면 x=x+1
			if y in C: x=x+1
		y=B[i]
		while y <=x:
			if y in C:
				x=x+1
			y=y+1
		A[i]=x
		C.add(A[i])
	return A

B = [int(x) for x in input().split()]
A = reconstruct(B)
print(A)