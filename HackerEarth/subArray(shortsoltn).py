N = int(input())
K_original = int(input())
array = list(map(int, input().rstrip().split()))
max_len = 0
for i in range(0,N-1):
	pos = i
	lenOfSub = 0
	K = K_original
	for j in range(i+1,N):
		if K >= 0:
			diff = abs(array[pos] - array[j])
			if array[j] > array[pos] :
				pos = j
				K = K - (j - i)*diff
			else:
				K = K - diff
			lenOfSub += 1
		else:
			lenOfSub -= 1
			break
	max_len = max(lenOfSub,max_len)
print(max_len+1)