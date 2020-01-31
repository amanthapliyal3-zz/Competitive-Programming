'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
# Write your code here
T = int(input())
result = [] #for storing results

def findMinChoc(C, N) :
    temp = min_left = 0
    first_share = 0
    temp =  (2*C - (N * (N - 1)))
    print(temp)
    if temp//(2*N) < 1:
        min_left = C
    else :
        first_share = temp//(2*N)
        print(first_share)
        min_left = C - ((2*first_share + (N-1))*N)//2
        print(min_left)
    return min_left


for i in range(T) :
   # input_str = input()
    input_str = list(map(int,input().rstrip().split()))
    C = int(input_str[0])
    N = int(input_str[1])
    print(C, N)
    
    #find Minimum Chocolates left
    
    result.append(findMinChoc(C, N))

for each in result:
    print(each)
    
    