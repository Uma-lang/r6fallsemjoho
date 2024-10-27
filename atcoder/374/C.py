def main():
    N = int(input())
    K = list(map(int, input().split()))
    totalsum = sum(K)
    minDif = totalsum

    for mask in range(1 << N):
        sumA = 0
        for i in range(N):
            if mask & (1 << i):
                sumA += K[i]
    
        sumB = totalsum - sumA
        maxGroupSize = max(sumA, sumB)
        minDif = min(minDif, maxGroupSize)
    
    print(minDif)

if __name__ == "__main__":
    main()