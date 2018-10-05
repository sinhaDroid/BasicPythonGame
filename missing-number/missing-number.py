# getMissingNo takes list as argument
def getMissingNo(A):
    n = len(A)
    total = (n+1)*(n+2)/2
    sum_of_A = sum(A)
    return int(total - sum_of_A)

# Driver Code
arr = list(map(int, input().split(" ")))
print(arr)

print(getMissingNo(arr))