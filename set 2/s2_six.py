# navi approch solve this question
def findPairNaive(A, N, X):

    for i in range(N):
        for j in range(i + 1, N):
            if A[i] + A[j] == X:
                return "Yes"  
    return "No"  