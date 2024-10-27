def main():
    N = int(input())
    A = []
    genso = 1
    for i in range(N):
        row = list(map(int, input().split()))
        A.append(row)
    for i in range(N):
        if genso-1 >= i:
            genso = A[genso - 1][i]
        else:
            genso = A[i][genso - 1]
    print(genso)
if __name__ == "__main__":
    main()    