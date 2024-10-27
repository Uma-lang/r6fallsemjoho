def main():
    S = input()
    X = [0] * 26
    for i in range(26):
        X[ord(S[i]) - ord('A')] = i
    ans = 0
    for i in range(25):
        sub = abs(X[i] - X[i + 1])
        ans += sub
    print(ans)
    
if __name__ == "__main__":
    main()