from sys import stdin, stdout

def checkPoints(N,C,L) :
	stack = [0]
	j = 0
	sum = 0
	while(j < N) :
		if C[stack[-1]]*L[j] > C[j]*L[j] :
			stack.append(j)
			sum = sum + C[j]*L[j]
		else :
			sum = sum + C[stack[-1]]*L[j]
		j = j + 1
	print(sum)


        
T = int(input())

for _ in range(T):
    N = int(input())
    C = list(map(int,stdin.readline().strip().split()))
    L = list(map(int, stdin.readline().strip().split()))
    checkPoints(N,C,L)
    