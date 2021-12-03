import sys
input = sys.stdin.readline

def bubbleSort(A):
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                count += 1
    return count

data = [int(x) for x in input().split()]
print(bubbleSort(data))